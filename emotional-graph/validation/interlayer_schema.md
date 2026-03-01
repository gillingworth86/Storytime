# Inter-Layer Edge Schema and Connection Map

## Purpose
Defines the valid connection types between layers, the rules governing them, and maps the primary inter-layer connections. This is the connective tissue of the graph – the architecture that makes it a causal system rather than four isolated taxonomies.

---

## Inter-Layer Edge Types

### Type 1: ACTIVATES (Drive → State)
**Direction:** Layer 1 → Layer 2  
**Meaning:** A drive, when threatened, deprived, or satisfied, triggers a corresponding internal state.  
**Sub-types:**
- `threat` – drive is threatened or under attack (e.g. SAF threatened → Anxiety)
- `deprivation` – drive is chronically unmet (e.g. BEL deprived → Loneliness)
- `satisfaction` – drive is fulfilled (e.g. CMP satisfied → Pride)
- `activation` – drive is positively stimulated without prior deprivation (e.g. NOV activated → Curiosity)

**Rule:** A drive can produce multiple states depending on the sub-type of activation. The same state can be produced by multiple drives.

---

### Type 2: SENSITISES (Trait → State)
**Direction:** Layer 3 → Layer 2  
**Meaning:** A trait raises or lowers the activation threshold for a state, or amplifies/dampens its intensity when activated.  
**Sub-types:**
- `lowers_threshold` – trait makes state easier to activate (e.g. low Emotional Stability → Anxiety activates more readily)
- `raises_threshold` – trait makes state harder to activate (e.g. high Resilience → Shame duration shortened)
- `amplifies` – trait intensifies the state when activated
- `dampens` – trait reduces the intensity of the state

**Rule:** Sensitisation edges do not create states – they modulate the conditions under which drives produce them.

---

### Type 3: EXPRESSES AS (State → Behaviour)
**Direction:** Layer 2 → Layer 4  
**Meaning:** A state, under pressure to discharge, produces a behaviour. This connection is always mediated by traits – the same state produces different behaviours depending on trait configuration.  
**Notation:** State → [Trait modulation] → Behaviour

**Rule:** No direct State → Behaviour edge without specifying the trait mediator. Where a state reliably produces a behaviour regardless of trait configuration, the trait mediator is noted as "trait-invariant."

---

### Type 4: MODULATES (Trait → Behaviour)
**Direction:** Layer 3 → Layer 4  
**Meaning:** A trait shapes which behaviour a state produces, or amplifies/suppresses a behaviour's likelihood.  
**Sub-types:**
- `selects` – trait determines which behaviour a state produces (e.g. high Sincerity + Vulnerability → Vulnerability Disclosure rather than Deflecting)
- `amplifies` – trait increases the frequency or intensity of a behaviour
- `suppresses` – trait decreases the likelihood of a behaviour

**Rule:** Modulation edges must reference a state context – a trait modulates behaviour *in the context of a state*, not in the abstract.

---

### Type 5: REINFORCES (Behaviour → State) [Feedback – longitudinal mode]
**Direction:** Layer 4 → Layer 2  
**Meaning:** A behaviour, once enacted, generates or intensifies a state. Operates primarily in longitudinal mode.  
**Examples:** Acting confidently generates Pride; repeated Withdrawing deepens Loneliness; Vulnerability Disclosure met with acceptance reduces Anxiety.

**Rule:** Feedback edges are typed distinctly and inactive in first-response analytical mode.

---

### Type 6: SHAPES (State → Trait) [Feedback – longitudinal mode]
**Direction:** Layer 2 → Layer 3  
**Meaning:** Repeated or chronic state experience reshapes stable trait dispositions over time.  
**Examples:** Chronic Anxiety → increases Control-seeking and decreases Risk Tolerance; repeated experiences of Flow → increases trait Curiosity; chronic Shame → reduces Vulnerability Tolerance.

**Rule:** Longitudinal mode only. The mechanism is repetition over time, not single activation events.

---

## Primary Inter-Layer Connection Map

### Drive → State (ACTIVATES)

#### Belonging (BEL)
| Activation sub-type | State |
|---|---|
| Threat | Anxiety, Shame, Jealousy |
| Deprivation | Loneliness, Grief |
| Satisfaction | Pride (partial) |
| Activation | Excitement (social) |

#### Status (STA)
| Activation sub-type | State |
|---|---|
| Threat | Shame, Envy, Defensiveness, Anxiety |
| Deprivation | Resentment (status deprivation chronic) |
| Satisfaction | Pride |

#### Safety (SAF)
| Activation sub-type | State |
|---|---|
| Threat | Anxiety, Vulnerability, Defensiveness |
| Existential threat | Mortality Salience |
| Deprivation | Resentment (chronic unsafe environment) |

#### Autonomy (AUT)
| Activation sub-type | State |
|---|---|
| Threat/Violation | Anger |
| Chronic violation | Resentment |
| Satisfaction | Flow (partial) |

#### Meaning (MEA)
| Activation sub-type | State |
|---|---|
| Threat/Collapse | Anxiety (existential) |
| Activation | Inspiration, Awe |
| Satisfaction | Flow (partial) |

#### Competence (CMP)
| Activation sub-type | State |
|---|---|
| Threat/Failure | Anxiety, Shame |
| Activation | Curiosity |
| Satisfaction | Pride, Flow (partial) |

#### Recognition (REC)
| Activation sub-type | State |
|---|---|
| Threat/Absence | Shame, Loneliness |
| Satisfaction | Pride |

#### Play (PLA)
| Activation sub-type | State |
|---|---|
| Deprivation | Boredom |
| Activation | Excitement, Flow (partial) |

#### Novelty (NOV)
| Activation sub-type | State |
|---|---|
| Deprivation | Boredom |
| Activation | Curiosity, Excitement |

#### Transcendence (TRN)
| Activation sub-type | State |
|---|---|
| Activation | Awe, Flow (partial) |
| Threat (mortality) | Mortality Salience (indirect, via SAF) |

#### Contribution (CON)
| Activation sub-type | State |
|---|---|
| Violation/Failure | Guilt |
| Activation | Inspiration |
| Satisfaction | Pride (partial) |

---

### Trait → State (SENSITISES) – Key Connections

| Trait | State | Sub-type | Mechanism |
|---|---|---|---|
| Emotional Stability (low) | Anxiety | lowers_threshold | Lower baseline stability means SAF threats activate anxiety more readily |
| Emotional Stability (low) | Shame | lowers_threshold | Self-concept more vulnerable to status/belonging threats |
| Emotional Stability (low) | Anger | amplifies | State intensity increased |
| Resilience (high) | Shame | raises_threshold | Recovery from shame faster; duration shortened |
| Resilience (high) | Grief | raises_threshold | Recovery rate increased |
| Resilience (high) | Resentment | raises_threshold | Chronic negative states less likely to calcify |
| Empathy (high) | Guilt | lowers_threshold | Greater sensitivity to others' states means norm violations register more readily |
| Empathy (high) | Shame | lowers_threshold | Social sensitivity increases exposure to social pain |
| Risk Tolerance (high) | Anxiety | raises_threshold | Comfort with uncertainty means SAF threats activate anxiety less readily |
| Risk Tolerance (high) | Excitement | lowers_threshold | Same novel situation produces excitement rather than anxiety |
| Vulnerability Tolerance (high) | Vulnerability | dampens | Exposure state less aversive and shorter |
| Fairness-orientation (high) | Anger | lowers_threshold | Inequity violations activate anger more readily |
| Fairness-orientation (high) | Resentment | lowers_threshold | Chronic unfairness calcifies more readily |
| Control-seeking (high) | Anxiety | raises_threshold | Environmental management reduces uncertainty threat |
| Control-seeking (high) | Jealousy | amplifies | Belonging threats activate control state more intensely |
| Openness (high) | Curiosity | lowers_threshold | Novelty activates curiosity more readily |
| Openness (high) | Boredom | raises_threshold | Greater range of engagement means deprivation takes longer to register |
| Conscientiousness (high) | Guilt | amplifies | Norm violation registers more intensely |
| Curiosity trait (high) | Curiosity state | lowers_threshold | Exploratory motivation is easier to activate |

---

### State → Behaviour (EXPRESSES AS) with Trait Mediation

Key pathways – format: State + Trait configuration → Behaviour

#### Anxiety
| Trait configuration | Behaviour |
|---|---|
| High Agreeableness | Placating, Seeking Reassurance |
| High Dominance | Controlling Behaviour, Deflecting |
| High Risk Tolerance | Challenging (confront the threat) |
| Low Emotional Stability | Withdrawing |
| High Extraversion | Attention-seeking (anxiety displaced) |
| Trait-invariant (high anxiety) | Seeking Reassurance |

#### Shame
| Trait configuration | Behaviour |
|---|---|
| High Sincerity + High Vulnerability Tolerance | Vulnerability Disclosure |
| Low Sincerity | Performing, Deflecting |
| High Dominance | Anger → Challenging (shame converted) |
| High Agreeableness | Placating, Withdrawing |
| Low Vulnerability Tolerance | Withdrawing |

#### Guilt
| Trait configuration | Behaviour |
|---|---|
| High Empathy + High Conscientiousness | Helping/Caregiving, Vulnerability Disclosure |
| Low Empathy | Placating (surface-level appeasement only) |
| High Sincerity | Vulnerability Disclosure, direct apology |
| Low Conscientiousness | Withdrawing, Deflecting |

#### Anger
| Trait configuration | Behaviour |
|---|---|
| High Dominance + High Assertiveness | Challenging, Dominating |
| High Agreeableness | Deflecting, Placating (suppressed) |
| High Sincerity | Challenging (direct) |
| Low Emotional Stability | Controlling Behaviour, Dominating |
| High Resilience | Boundary-Setting (contained expression) |

#### Loneliness
| Trait configuration | Behaviour |
|---|---|
| High Extraversion | Attention-seeking, Performing |
| High Vulnerability Tolerance | Vulnerability Disclosure, Intimacy-building |
| Low Vulnerability Tolerance | Mirroring (proximity without exposure) |
| High Agreeableness | Conforming (belonging through compliance) |

#### Vulnerability
| Trait configuration | Behaviour |
|---|---|
| High Vulnerability Tolerance + High Sincerity | Vulnerability Disclosure |
| Low Vulnerability Tolerance | Deflecting, Withdrawing |
| High Control-seeking | Controlling Behaviour (managing exposure) |
| High Charm | Performing (vulnerability performed rather than disclosed) |

#### Resentment
| Trait configuration | Behaviour |
|---|---|
| High Dominance | Challenging, Dominating |
| High Agreeableness | Withdrawing, Conforming (passive) |
| High Assertiveness + High Fairness-orientation | Boundary-setting, Challenging |
| Low Emotional Stability | Controlling Behaviour |

#### Inspiration
| Trait configuration | Behaviour |
|---|---|
| High Extraversion | Storytelling, Performing |
| High Conscientiousness | Collaborating, Nurturing |
| High Empathy | Helping/Caregiving, Nurturing |
| High Sincerity | Vulnerability Disclosure (sharing the inspiration source) |

#### Envy
| Trait configuration | Behaviour |
|---|---|
| High Dominance | Competing, Signalling Status |
| High Openness | Inspiration path → Collaborating |
| Low Emotional Stability | Attention-seeking, Challenging |
| High Fairness-orientation | Challenging (reframed as unfairness) |

#### Pride
| Trait configuration | Behaviour |
|---|---|
| High Extraversion | Storytelling, Signalling Status |
| High Sincerity | Storytelling (authentic sharing) |
| Low Sincerity | Performing, Signalling Status (strategic display) |
| High Empathy | Nurturing, Helping (pride channelled toward others) |

#### Flow
| Trait configuration | Behaviour |
|---|---|
| Trait-invariant | Collaborating or sustained task engagement |
| High Extraversion | Storytelling (sharing the experience after) |

---

### Trait → Behaviour (MODULATES) – Key Amplification/Suppression

| Trait | Behaviour | Effect | Mechanism |
|---|---|---|---|
| Charm (high) | Mirroring | amplifies | Social fluency makes mirroring more natural and effective |
| Charm (high) | Performing | amplifies | Performance quality increased |
| Sincerity (high) | Vulnerability Disclosure | amplifies | Authentic orientation makes disclosure more likely |
| Sincerity (high) | Performing | suppresses | Authentic orientation resists self-curation |
| Empathy (high) | Mirroring | amplifies | Resonance makes mirroring more accurate |
| Empathy (high) | Nurturing | amplifies | Sensitivity to others' states drives developmental support |
| Empathy (high) | Dominating | suppresses | Awareness of others' experience inhibits subordination |
| Dominance (high) | Challenging | amplifies | Hierarchy assertion amplifies targeted opposition |
| Dominance (high) | Collaborating | suppresses (mild) | Control orientation constrains joint-effort mode |
| Agreeableness (high) | Placating | amplifies | Harmony-seeking drives appeasement |
| Agreeableness (high) | Challenging | suppresses | Conflict avoidance inhibits direct opposition |
| Assertiveness (high) | Boundary-setting | amplifies | Direct self-expression amplifies limit-assertion |
| Extraversion (high) | Attention-seeking | amplifies | Social energy orientation drives focus-seeking |
| Extraversion (high) | Storytelling | amplifies | Social mode amplifies narrative self-presentation |
| Extraversion (high) | Withdrawing | suppresses | Social energy orientation makes withdrawal aversive |
| Resilience (high) | Withdrawing | suppresses | Recovery capacity reduces duration of withdrawal |
| Risk Tolerance (high) | Vulnerability Disclosure | amplifies | Comfort with uncertain outcomes enables exposure |
| Risk Tolerance (high) | Conforming | suppresses | Comfort with difference reduces norm-alignment pressure |
| Control-seeking (high) | Controlling Behaviour | amplifies | Direct expression of the disposition |
| Control-seeking (high) | Collaborating | suppresses | Joint effort requires relinquishing control |
| Fairness-orientation (high) | Challenging | amplifies | Inequity perception drives targeted opposition |
| Humour (high) | Deflecting | amplifies | Levity is a primary deflection mechanism |
| Humour (high) | Mirroring | amplifies | Shared levity is a rapport mechanism |
| Vulnerability Tolerance (high) | Intimacy-building | amplifies | Capacity for exposure enables progressive disclosure |
| Openness (high) | Collaborating | amplifies | Receptivity to others' perspectives enables joint effort |
| Conscientiousness (high) | Helping/Caregiving | amplifies | Follow-through orientation ensures support is delivered |

---

## Feedback Edges (Longitudinal Mode Only)

### Behaviour → State (REINFORCES)

| Behaviour | State | Effect | Mechanism |
|---|---|---|---|
| Withdrawing (repeated) | Loneliness | generates | Reduced engagement deepens belonging deprivation |
| Vulnerability Disclosure (met with acceptance) | Anxiety | suppresses | Successful exposure reduces safety threat |
| Vulnerability Disclosure (met with rejection) | Shame | generates | Failed exposure triggers shame |
| Performing (habitual) | Shame | generates (delayed) | Gap between performed and authentic self widens |
| Competing (winning) | Pride | generates | Achievement confirms competence and status |
| Competing (losing) | Shame/Anxiety | generates | Failure threatens status and competence |
| Helping/Caregiving | Inspiration | reinforces | Prosocial action generates meaning activation |
| Controlling Behaviour | Resentment (in target) | generates | Constraint violation activates resentment in the controlled party |
| Intimacy-building | Loneliness | suppresses | Progressive disclosure resolves belonging deprivation |
| Challenging (successfully) | Pride | generates | Effective opposition confirms competence and autonomy |
| Conforming (habitual) | Resentment | generates (delayed) | Chronic self-suppression activates autonomy violation |

### State → Trait (SHAPES) [Longitudinal]

| State (chronic/repeated) | Trait | Effect | Mechanism |
|---|---|---|---|
| Anxiety (chronic) | Emotional Stability | lowers | Repeated activation habituates nervous system toward threat detection |
| Anxiety (chronic) | Risk Tolerance | lowers | Repeated threat experience increases uncertainty aversion |
| Anxiety (chronic) | Control-seeking | raises | Control is developed as an anxiety management mechanism |
| Shame (repeated) | Vulnerability Tolerance | lowers | Repeated exposure pain builds avoidance disposition |
| Shame (repeated) | Sincerity | lowers | Authentic expression becomes associated with pain |
| Flow (repeated) | Curiosity (trait) | raises | Repeated rewarding exploration strengthens exploratory disposition |
| Flow (repeated) | Openness | raises | Repeated positive novelty experience increases receptivity |
| Pride (repeated) | Emotional Stability | raises | Accumulated competence and status satisfaction stabilises baseline |
| Inspiration (repeated) | Conscientiousness | raises | Meaning-driven action builds follow-through disposition |
| Resentment (chronic) | Agreeableness | lowers | Suppressed anger erodes accommodation disposition |
| Resentment (chronic) | Assertiveness | raises or lowers | Depending on expression path: confrontation or collapse |
| Guilt (repeated + resolved) | Empathy | raises | Reparative cycles deepen sensitivity to others' states |
| Loneliness (chronic) | Warmth | lowers | Prolonged isolation erodes positive orientation toward others |
| Vulnerability (accepted repeatedly) | Vulnerability Tolerance | raises | Safe exposure experiences build tolerance disposition |

---

## Structural Notes

**The diagnostic pathway** (first-response mode): observe Behaviour → identify probable State → apply Trait filter to understand why that state produced that behaviour → trace back to activating Drive. Context (provided at prompt time) narrows the probable states and traits.

**The expression pathway** (first-response mode): Drive is threatened or activated → State is triggered → Trait configuration selects which Behaviour the state produces.

**The development pathway** (longitudinal mode): Behaviour → reinforces/generates State → repeated State → shapes Trait → altered Trait changes future State activation thresholds and Behaviour selection.

**Multi-drive activations:** Most social situations activate multiple drives simultaneously. The resulting state is typically the most intense activation, but co-activation patterns produce complex states (e.g. a performance review activates STA + CMP + SAF simultaneously → Anxiety + Defensiveness + Pride depending on the outcome, all modulated by trait configuration).
