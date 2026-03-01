import json
import sys
from pathlib import Path

GRAPH_FILE = Path(__file__).parent.parent / "graph" / "graph.json"

VALID_INTRA_RELATIONSHIPS = {
    "1": {"complementarity", "conflict", "conditional", "neutral"},
    "2": {"triggers", "suppresses", "co_occurs"},
    "3": {"potentiates", "inhibits", "correlates"},
    "4": {"escalates", "substitutes", "inhibits"}
}

VALID_STATUSES = {"confirmed", "provisional"}
VALID_RESEARCH_SUPPORT = {"strong", "moderate", "weak"}
VALID_INTER_TYPES = {"activates", "sensitises", "expresses_as", "modulates", "reinforces", "shapes"}
VALID_ACTIVATE_SUBTYPES = {"threat", "deprivation", "satisfaction", "activation", "exposure", "violation", "loss", "existential_threat", "chronic_violation"}
VALID_SENSITISE_SUBTYPES = {"lowers_threshold", "raises_threshold", "amplifies", "dampens"}
VALID_MODULATE_EFFECTS = {"amplifies", "suppresses"}


def load_graph(path):
    with open(path) as f:
        return json.load(f)


def get_all_node_ids(graph):
    ids = {}
    for layer_id, layer in graph.get("layers", {}).items():
        ids[layer_id] = set(layer.get("nodes", {}).keys())
    return ids


def validate_node(node_id, node, layer_id):
    errors = []
    if not node.get("name"):
        errors.append(f"[L{layer_id}/{node_id}] Missing 'name'")
    if not node.get("description"):
        errors.append(f"[L{layer_id}/{node_id}] Missing 'description'")
    if node.get("status") not in VALID_STATUSES:
        errors.append(f"[L{layer_id}/{node_id}] Invalid status '{node.get('status')}'")
    if layer_id == "1" and node.get("research_support") not in VALID_RESEARCH_SUPPORT:
        errors.append(f"[L{layer_id}/{node_id}] Invalid research_support '{node.get('research_support')}'")
    if node.get("id") and node.get("id") != node_id:
        errors.append(f"[L{layer_id}/{node_id}] id field '{node.get('id')}' does not match key")
    return errors


def validate_intra_edge(edge, layer_id, node_ids, index):
    errors = []
    prefix = f"[L{layer_id}/IntraEdge{index}]"
    valid_rels = VALID_INTRA_RELATIONSHIPS.get(layer_id, set())

    source = edge.get("source")
    target = edge.get("target")
    rel = edge.get("relationship")

    if not source:
        errors.append(f"{prefix} Missing 'source'")
    elif source not in node_ids:
        errors.append(f"{prefix} Source '{source}' not in layer {layer_id} nodes")

    if not target:
        errors.append(f"{prefix} Missing 'target'")
    elif target not in node_ids:
        errors.append(f"{prefix} Target '{target}' not in layer {layer_id} nodes")

    if source and target and source == target:
        errors.append(f"{prefix} Self-loop on '{source}'")

    if rel not in valid_rels:
        errors.append(f"{prefix} Invalid relationship '{rel}' for layer {layer_id}. Valid: {valid_rels}")

    if rel == "conditional" and not edge.get("condition"):
        errors.append(f"{prefix} Conditional edge missing 'condition'")

    if layer_id in ("1",) and not edge.get("mechanism"):
        errors.append(f"{prefix} Missing 'mechanism'")

    return errors


def check_duplicate_edges(edges, layer_id):
    errors = []
    seen = set()
    for i, edge in enumerate(edges):
        source = edge.get("source", "")
        target = edge.get("target", "")
        rel = edge.get("relationship", "")
        key = (tuple(sorted([source, target])), rel)
        if key in seen:
            errors.append(f"[L{layer_id}/IntraEdge{i}] Duplicate edge ({rel}) between '{source}' and '{target}'")
        seen.add(key)
    return errors


def validate_layer(layer_id, layer):
    errors = []
    nodes = layer.get("nodes", {})
    node_ids = set(nodes.keys())

    for node_id, node in nodes.items():
        errors.extend(validate_node(node_id, node, layer_id))

    intra_edges = layer.get("edges", {}).get("intra_layer", [])
    for i, edge in enumerate(intra_edges):
        errors.extend(validate_intra_edge(edge, layer_id, node_ids, i))
    errors.extend(check_duplicate_edges(intra_edges, layer_id))

    return errors


def validate_inter_layer_edges(graph, all_node_ids):
    errors = []
    inter = graph.get("inter_layer_edges", {})

    drive_ids = all_node_ids.get("1", set())
    state_ids = all_node_ids.get("2", set())
    trait_ids = all_node_ids.get("3", set())
    behaviour_ids = all_node_ids.get("4", set())

    for i, edge in enumerate(inter.get("drive_to_state", [])):
        prefix = f"[Inter/DriveState{i}]"
        if edge.get("drive") not in drive_ids:
            errors.append(f"{prefix} Drive '{edge.get('drive')}' not in Layer 1")
        if edge.get("state") not in state_ids:
            errors.append(f"{prefix} State '{edge.get('state')}' not in Layer 2")
        if edge.get("sub_type") not in VALID_ACTIVATE_SUBTYPES:
            errors.append(f"{prefix} Invalid sub_type '{edge.get('sub_type')}'")

    for i, edge in enumerate(inter.get("trait_to_state", [])):
        prefix = f"[Inter/TraitState{i}]"
        if edge.get("trait") not in trait_ids:
            errors.append(f"{prefix} Trait '{edge.get('trait')}' not in Layer 3")
        if edge.get("state") not in state_ids:
            errors.append(f"{prefix} State '{edge.get('state')}' not in Layer 2")
        if edge.get("sub_type") not in VALID_SENSITISE_SUBTYPES:
            errors.append(f"{prefix} Invalid sub_type '{edge.get('sub_type')}'")

    for i, edge in enumerate(inter.get("state_to_behaviour", [])):
        prefix = f"[Inter/StateBehaviour{i}]"
        if edge.get("state") not in state_ids:
            errors.append(f"{prefix} State '{edge.get('state')}' not in Layer 2")
        if edge.get("behaviour") not in behaviour_ids:
            errors.append(f"{prefix} Behaviour '{edge.get('behaviour')}' not in Layer 4")
        if not edge.get("trait_condition"):
            errors.append(f"{prefix} Missing 'trait_condition'")

    for i, edge in enumerate(inter.get("trait_to_behaviour_modulation", [])):
        prefix = f"[Inter/TraitBehaviour{i}]"
        if edge.get("trait") not in trait_ids:
            errors.append(f"{prefix} Trait '{edge.get('trait')}' not in Layer 3")
        if edge.get("behaviour") not in behaviour_ids:
            errors.append(f"{prefix} Behaviour '{edge.get('behaviour')}' not in Layer 4")
        if edge.get("effect") not in VALID_MODULATE_EFFECTS:
            errors.append(f"{prefix} Invalid effect '{edge.get('effect')}'")

    for i, edge in enumerate(inter.get("feedback_behaviour_to_state", [])):
        prefix = f"[Inter/FeedbackB2S{i}]"
        if edge.get("behaviour") not in behaviour_ids:
            errors.append(f"{prefix} Behaviour '{edge.get('behaviour')}' not in Layer 4")
        if edge.get("state") not in state_ids:
            errors.append(f"{prefix} State '{edge.get('state')}' not in Layer 2")
        if edge.get("mode") != "longitudinal":
            errors.append(f"{prefix} Feedback edge must have mode 'longitudinal'")

    for i, edge in enumerate(inter.get("feedback_state_to_trait", [])):
        prefix = f"[Inter/FeedbackS2T{i}]"
        if edge.get("state") not in state_ids:
            errors.append(f"{prefix} State '{edge.get('state')}' not in Layer 2")
        if edge.get("trait") not in trait_ids:
            errors.append(f"{prefix} Trait '{edge.get('trait')}' not in Layer 3")
        if edge.get("mode") != "longitudinal":
            errors.append(f"{prefix} Feedback edge must have mode 'longitudinal'")

    return errors


def validate_discard_register(register):
    errors = []
    for i, entry in enumerate(register):
        if not entry.get("candidate"):
            errors.append(f"[Discard{i}] Missing 'candidate'")
        if not entry.get("reason"):
            errors.append(f"[Discard{i}] Missing 'reason'")
        dest = entry.get("destination", "")
        if not any(dest.startswith(f"Layer {n}") for n in ["1", "2", "3", "4"]) and not dest.startswith("None") and not dest.startswith("Merged") and not dest.startswith("Emergent") and not dest.startswith("Integration") and not dest.startswith("Context"):
            errors.append(f"[Discard{i}] Destination '{dest}' does not reference a valid layer or accepted value")
    return errors


def count_inter_edges(inter):
    total = 0
    for key, edges in inter.items():
        total += len(edges)
    return total


def validate_graph(graph):
    results = {"passed": True, "layers": {}, "inter_layer": {}, "discard": {}, "summary": {}}
    all_node_ids = get_all_node_ids(graph)

    for layer_id, layer in graph.get("layers", {}).items():
        errors = validate_layer(layer_id, layer)
        node_count = len(layer.get("nodes", {}))
        edge_count = len(layer.get("edges", {}).get("intra_layer", []))
        results["layers"][layer_id] = {
            "name": layer.get("name"),
            "nodes": node_count,
            "intra_edges": edge_count,
            "errors": errors,
            "status": "PASS" if not errors else "FAIL"
        }
        if errors:
            results["passed"] = False

    inter_errors = validate_inter_layer_edges(graph, all_node_ids)
    inter_edge_count = count_inter_edges(graph.get("inter_layer_edges", {}))
    results["inter_layer"] = {
        "total_edges": inter_edge_count,
        "errors": inter_errors,
        "status": "PASS" if not inter_errors else "FAIL"
    }
    if inter_errors:
        results["passed"] = False

    discard_errors = validate_discard_register(graph.get("discard_register", []))
    results["discard"] = {
        "entries": len(graph.get("discard_register", [])),
        "errors": discard_errors,
        "status": "PASS" if not discard_errors else "FAIL"
    }
    if discard_errors:
        results["passed"] = False

    total_errors = (
        sum(len(v["errors"]) for v in results["layers"].values())
        + len(inter_errors)
        + len(discard_errors)
    )

    total_nodes = sum(v["nodes"] for v in results["layers"].values())
    total_intra = sum(v["intra_edges"] for v in results["layers"].values())

    results["summary"] = {
        "overall": "PASS" if results["passed"] else "FAIL",
        "total_errors": total_errors,
        "total_nodes": total_nodes,
        "total_intra_edges": total_intra,
        "total_inter_edges": inter_edge_count
    }

    return results


def print_results(results):
    print("\n" + "=" * 60)
    print("EMOTIONAL GRAPH VALIDATOR")
    print("=" * 60)

    for layer_id, lr in results["layers"].items():
        sym = "✓" if lr["status"] == "PASS" else "✗"
        print(f"\n{sym} Layer {layer_id}: {lr['name']}")
        print(f"  Nodes: {lr['nodes']} | Intra-layer edges: {lr['intra_edges']}")
        for e in lr["errors"]:
            print(f"  ERROR: {e}")

    il = results["inter_layer"]
    sym = "✓" if il["status"] == "PASS" else "✗"
    print(f"\n{sym} Inter-layer edges ({il['total_edges']} total)")
    for e in il["errors"]:
        print(f"  ERROR: {e}")

    dr = results["discard"]
    sym = "✓" if dr["status"] == "PASS" else "✗"
    print(f"\n{sym} Discard register ({dr['entries']} entries)")
    for e in dr["errors"]:
        print(f"  ERROR: {e}")

    s = results["summary"]
    print("\n" + "-" * 60)
    print(f"RESULT: {s['overall']}")
    print(f"Total errors: {s['total_errors']}")
    print(f"Total nodes: {s['total_nodes']} | Intra-edges: {s['total_intra_edges']} | Inter-edges: {s['total_inter_edges']}")
    print("=" * 60 + "\n")


def main():
    path = GRAPH_FILE
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: graph file not found at {path}")
        sys.exit(1)
    graph = load_graph(path)
    results = validate_graph(graph)
    print_results(results)
    sys.exit(0 if results["passed"] else 1)


if __name__ == "__main__":
    main()
