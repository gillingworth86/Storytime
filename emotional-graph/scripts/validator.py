import json
import sys
from pathlib import Path

GRAPH_FILE = Path(__file__).parent.parent / "graph" / "graph.json"

LAYER_NAMES = {
    "1": "Drives",
    "2": "States",
    "3": "Traits",
    "4": "Behaviours"
}

VALID_RELATIONSHIPS = {"complementarity", "conflict", "conditional", "neutral"}
VALID_STATUSES = {"confirmed", "provisional"}
VALID_RESEARCH_SUPPORT = {"strong", "moderate", "weak"}


def load_graph(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def validate_node(node_id: str, node: dict, layer_id: str, all_node_ids: set) -> list[str]:
    errors = []

    if not node.get("name"):
        errors.append(f"[{node_id}] Missing 'name'")
    if not node.get("description"):
        errors.append(f"[{node_id}] Missing 'description'")
    if node.get("status") not in VALID_STATUSES:
        errors.append(f"[{node_id}] Invalid status '{node.get('status')}' - must be one of {VALID_STATUSES}")
    if node.get("research_support") not in VALID_RESEARCH_SUPPORT:
        errors.append(f"[{node_id}] Invalid research_support '{node.get('research_support')}' - must be one of {VALID_RESEARCH_SUPPORT}")
    if node.get("id") != node_id:
        errors.append(f"[{node_id}] Node id field '{node.get('id')}' does not match key '{node_id}'")

    return errors


def validate_edge(edge: dict, layer_id: str, node_ids: set, edge_index: int) -> list[str]:
    errors = []
    prefix = f"[Edge {edge_index} L{layer_id}]"

    source = edge.get("source")
    target = edge.get("target")
    relationship = edge.get("relationship")

    if not source:
        errors.append(f"{prefix} Missing 'source'")
    elif source not in node_ids:
        errors.append(f"{prefix} Source '{source}' not a valid node in layer {layer_id}")

    if not target:
        errors.append(f"{prefix} Missing 'target'")
    elif target not in node_ids:
        errors.append(f"{prefix} Target '{target}' not a valid node in layer {layer_id}")

    if source and target and source == target:
        errors.append(f"{prefix} Self-loop detected on '{source}'")

    if relationship not in VALID_RELATIONSHIPS:
        errors.append(f"{prefix} Invalid relationship '{relationship}' - must be one of {VALID_RELATIONSHIPS}")

    if relationship == "conditional" and not edge.get("condition"):
        errors.append(f"{prefix} Conditional edge missing 'condition' description")

    if not edge.get("mechanism"):
        errors.append(f"{prefix} Missing 'mechanism' description")

    return errors


def check_duplicate_edges(edges: list) -> list[str]:
    errors = []
    seen = set()
    for i, edge in enumerate(edges):
        source = edge.get("source", "")
        target = edge.get("target", "")
        pair = tuple(sorted([source, target]))
        if pair in seen:
            errors.append(f"[Edge {i}] Duplicate edge between '{source}' and '{target}'")
        seen.add(pair)
    return errors


def check_discard_register(register: list) -> list[str]:
    errors = []
    valid_destinations = {f"Layer {n}: {name}" for n, name in LAYER_NAMES.items()}
    for i, entry in enumerate(register):
        if not entry.get("candidate"):
            errors.append(f"[Discard {i}] Missing 'candidate'")
        if not entry.get("reason"):
            errors.append(f"[Discard {i}] Missing 'reason'")
        dest = entry.get("destination", "")
        if not any(dest.startswith(f"Layer {n}") for n in LAYER_NAMES):
            errors.append(f"[Discard {i}] Destination '{dest}' does not reference a valid layer")
    return errors


def validate_layer(layer_id: str, layer: dict) -> list[str]:
    errors = []
    nodes = layer.get("nodes", {})
    node_ids = set(nodes.keys())

    for node_id, node in nodes.items():
        errors.extend(validate_node(node_id, node, layer_id, node_ids))

    intra_edges = layer.get("edges", {}).get("intra_layer", [])
    for i, edge in enumerate(intra_edges):
        errors.extend(validate_edge(edge, layer_id, node_ids, i))
    errors.extend(check_duplicate_edges(intra_edges))

    return errors


def validate_graph(graph: dict) -> dict:
    results = {
        "passed": True,
        "layers": {},
        "discard_register": [],
        "summary": {}
    }

    layers = graph.get("layers", {})
    for layer_id, layer in layers.items():
        layer_errors = validate_layer(layer_id, layer)
        node_count = len(layer.get("nodes", {}))
        edge_count = len(layer.get("edges", {}).get("intra_layer", []))
        results["layers"][layer_id] = {
            "name": layer.get("name"),
            "nodes": node_count,
            "edges": edge_count,
            "errors": layer_errors,
            "status": "PASS" if not layer_errors else "FAIL"
        }
        if layer_errors:
            results["passed"] = False

    discard_errors = check_discard_register(graph.get("discard_register", []))
    results["discard_register"] = {
        "entries": len(graph.get("discard_register", [])),
        "errors": discard_errors,
        "status": "PASS" if not discard_errors else "FAIL"
    }
    if discard_errors:
        results["passed"] = False

    total_errors = sum(
        len(v["errors"]) for v in results["layers"].values()
    ) + len(discard_errors)

    results["summary"] = {
        "overall": "PASS" if results["passed"] else "FAIL",
        "total_errors": total_errors,
        "layers_validated": len(layers),
        "discard_entries": len(graph.get("discard_register", []))
    }

    return results


def print_results(results: dict):
    print("\n" + "=" * 60)
    print("EMOTIONAL GRAPH VALIDATOR")
    print("=" * 60)

    for layer_id, layer_result in results["layers"].items():
        status = layer_result["status"]
        symbol = "✓" if status == "PASS" else "✗"
        print(f"\n{symbol} Layer {layer_id}: {layer_result['name']}")
        print(f"  Nodes: {layer_result['nodes']} | Intra-layer edges: {layer_result['edges']}")
        if layer_result["errors"]:
            for error in layer_result["errors"]:
                print(f"  ERROR: {error}")

    dr = results["discard_register"]
    symbol = "✓" if dr["status"] == "PASS" else "✗"
    print(f"\n{symbol} Discard Register ({dr['entries']} entries)")
    if dr["errors"]:
        for error in dr["errors"]:
            print(f"  ERROR: {error}")

    summary = results["summary"]
    print("\n" + "-" * 60)
    print(f"RESULT: {summary['overall']}")
    print(f"Total errors: {summary['total_errors']}")
    print(f"Layers validated: {summary['layers_validated']}")
    print("=" * 60 + "\n")


def main():
    graph_path = GRAPH_FILE
    if len(sys.argv) > 1:
        graph_path = Path(sys.argv[1])

    if not graph_path.exists():
        print(f"Error: graph file not found at {graph_path}")
        sys.exit(1)

    graph = load_graph(graph_path)
    results = validate_graph(graph)
    print_results(results)
    sys.exit(0 if results["passed"] else 1)


if __name__ == "__main__":
    main()
