# Communication Royalty OS Data Model v0.1

**Minimal Records for Trace-Based Value Circulation**

Status: Draft
Version: v0.1
Layer: Data Model
Related Documents:

* `docs/communication-royalty-os-architecture.md`
* `docs/v0.4-structural-diff.md`
* `docs/structural-rumination-layer-v0.1.md`

---

## 1. Overview

This document defines the minimal data model for Communication Royalty OS.

Communication Royalty OS is a trace-based value circulation architecture for AI-agent communications.
Its purpose is to record and structure value relationships generated through communication, including reference, summarization, inference, reuse, transformation, routing, and influence.

This data model defines the smallest record types required to move from architecture to implementation.

The five core records are:

```text
1. Communication Event
2. Trace Event
3. Value Relation
4. Policy Evaluation
5. Review Record
```

These records intentionally separate communication, detection, value structuring, policy evaluation, and review.

This separation prevents the system from automatically treating every trace as ownership, every similarity as reuse, or every value relation as compensation.

---

## 2. Core Principle

The central principle of this data model is:

```text
Detection is not attribution.
Attribution is not compensation.
Compensation is not automatic.
```

Communication Royalty OS records evidence and structures relationships.

It does not automatically decide value.

---

## 3. Minimal Lifecycle

The minimal lifecycle is:

```text
Communication Event
    |
    v
Trace Event
    |
    v
Value Relation
    |
    v
Policy Evaluation
    |
    v
Review Record
```

Each stage has a different responsibility.

```text
Communication Event
= A communication occurred.

Trace Event
= A possible trace was detected.

Value Relation
= A possible value relationship was structured.

Policy Evaluation
= Rules and boundaries were applied.

Review Record
= A human, governance process, or accountable review system recorded a conclusion.
```

---

## 4. Record Type 1: Communication Event

### 4.1 Definition

A Communication Event is a record of a meaningful communication between users, agents, systems, models, documents, or services.

It is the starting point of Communication Royalty OS.

A Communication Event does not assert value.

It only records that a communication occurred.

### 4.2 Examples

Examples of Communication Events include:

* A user sends a prompt to an AI agent.
* Agent A sends a summary to Agent B.
* Agent B requests a recommendation from Agent C.
* An AI system reads a document and generates a response.
* A routing agent sends a task to a specialized model.
* An agent receives external context before executing a transaction.

### 4.3 Minimal Fields

```text
communication_event_id
timestamp
source_actor
target_actor
communication_type
content_reference
context_reference
session_reference
metadata
```

### 4.4 Field Descriptions

| Field                    | Description                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| `communication_event_id` | Unique identifier for the communication event.                                                        |
| `timestamp`              | Time at which the event occurred or was recorded.                                                     |
| `source_actor`           | User, agent, model, system, document, or service that initiated the communication.                    |
| `target_actor`           | User, agent, model, system, document, or service that received the communication.                     |
| `communication_type`     | Type of communication, such as prompt, response, summary, reference, routing, or transaction_context. |
| `content_reference`      | Reference to the communicated content. This may be a URI, hash, internal ID, or redacted pointer.     |
| `context_reference`      | Optional reference to the surrounding context.                                                        |
| `session_reference`      | Optional session, thread, or transaction context.                                                     |
| `metadata`               | Additional non-core information.                                                                      |

### 4.5 Suggested Communication Types

```text
prompt
response
summary
reference
inference_request
inference_response
routing
transformation
recommendation
transaction_context
review_request
system_message
other
```

---

## 5. Record Type 2: Trace Event

### 5.1 Definition

A Trace Event records a detected signal that may indicate a value relationship.

A Trace Event is derived from one or more Communication Events.

A Trace Event does not prove attribution.

It records that a possible trace exists.

### 5.2 Examples

Examples of Trace Events include:

* A reference to a prior document is detected.
* A summary appears to reuse a previous output.
* A reasoning structure resembles an earlier record.
* A model response is influenced by a known prior trace.
* An agent repeats a decision pattern from a previous communication.
* A prompt injects a suspicious false attribution claim.

### 5.3 Minimal Fields

```text
trace_event_id
communication_event_id
trace_type
detected_source
detected_target
detection_method
confidence
evidence_reference
risk_flags
metadata
```

### 5.4 Field Descriptions

| Field                    | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------------- |
| `trace_event_id`         | Unique identifier for the trace event.                                           |
| `communication_event_id` | Communication Event from which the trace was detected.                           |
| `trace_type`             | Type of detected trace.                                                          |
| `detected_source`        | Possible source, contributor, document, model, agent, or prior trace.            |
| `detected_target`        | Output, communication, decision, or downstream event that may contain the trace. |
| `detection_method`       | Method used to detect the trace.                                                 |
| `confidence`             | Confidence score or qualitative confidence level.                                |
| `evidence_reference`     | Reference to supporting evidence.                                                |
| `risk_flags`             | Optional warnings such as false_attribution_risk or trace_poisoning_risk.        |
| `metadata`               | Additional non-core information.                                                 |

### 5.5 Suggested Trace Types

```text
reference
summary_reuse
structural_reuse
inference_influence
routing_influence
transformation
quotation
paraphrase
decision_influence
transaction_influence
false_attribution_signal
trace_poisoning_signal
other
```

### 5.6 Suggested Detection Methods

```text
explicit_reference
semantic_similarity
structural_similarity
metadata_link
hash_match
citation_match
model_reported_trace
human_reported_trace
policy_trigger
manual_review
other
```

### 5.7 Confidence Model

Confidence may be represented as either a numeric score or a qualitative level.

Recommended qualitative levels:

```text
low
medium
high
confirmed
disputed
unknown
```

Recommended numeric range:

```text
0.0 to 1.0
```

The system should not treat a high confidence trace as automatic compensation.

---

## 6. Record Type 3: Value Relation

### 6.1 Definition

A Value Relation structures a possible relationship between a trace and a contributor, source, system, prior communication, or downstream value event.

A Value Relation is not a payment instruction.

It is a structured relationship that may support review, attribution, governance, or future value circulation.

### 6.2 Examples

Examples of Value Relations include:

* A document contributed to an AI-generated summary.
* A prior prompt influenced a downstream recommendation.
* A model output was reused by another agent.
* A reasoning structure helped complete a transaction.
* A source was referenced but does not require compensation.
* A trace is too weak and should be marked for review.

### 6.3 Minimal Fields

```text
value_relation_id
trace_event_id
relation_type
source_entity
target_entity
contribution_type
contribution_scope
strength
status
review_required
metadata
```

### 6.4 Field Descriptions

| Field                | Description                                                                            |
| -------------------- | -------------------------------------------------------------------------------------- |
| `value_relation_id`  | Unique identifier for the value relation.                                              |
| `trace_event_id`     | Trace Event that supports this relation.                                               |
| `relation_type`      | Type of value relationship.                                                            |
| `source_entity`      | Possible contributor, source, model, document, user, or prior trace.                   |
| `target_entity`      | Output, decision, transaction, communication, or value event influenced by the source. |
| `contribution_type`  | Type of contribution made by the source.                                               |
| `contribution_scope` | Scope of the contribution.                                                             |
| `strength`           | Strength of the relationship.                                                          |
| `status`             | Current status of the relation.                                                        |
| `review_required`    | Whether human or governance review is required.                                        |
| `metadata`           | Additional non-core information.                                                       |

### 6.5 Suggested Relation Types

```text
referenced_by
summarized_by
reused_by
transformed_by
influenced
routed_to
derived_from
supports
contradicts
requires_review
not_applicable
other
```

### 6.6 Suggested Contribution Types

```text
knowledge
text
structure
reasoning
summary
classification
recommendation
decision_support
transaction_support
governance_signal
risk_signal
other
```

### 6.7 Suggested Contribution Scope

```text
local
session
document
repository
agent_network
transaction
governance_process
cross_system
unknown
```

### 6.8 Suggested Status Values

```text
detected
structured
pending_policy_evaluation
pending_review
reviewed
accepted
rejected
disputed
archived
```

### 6.9 Strength Model

Strength may be represented as qualitative or numeric.

Recommended qualitative values:

```text
weak
moderate
strong
confirmed
uncertain
```

Recommended numeric range:

```text
0.0 to 1.0
```

A strong relation does not automatically imply ownership or compensation.

---

## 7. Record Type 4: Policy Evaluation

### 7.1 Definition

A Policy Evaluation applies rules, thresholds, boundaries, and governance conditions to a Value Relation.

Its role is to prevent automatic overreach.

Policy Evaluation helps determine whether a relation should be ignored, reviewed, escalated, attributed, restricted, or prepared for future circulation.

### 7.2 Examples

Examples of Policy Evaluations include:

* A low-confidence trace is marked as non-actionable.
* A high-impact relation is sent to human review.
* A false attribution risk is detected.
* A relation is out of compensation scope.
* A reuse claim requires stronger evidence.
* A governance rule prevents automatic royalty assignment.

### 7.3 Minimal Fields

```text
policy_evaluation_id
value_relation_id
policy_profile
evaluation_result
boundary_flags
required_actions
review_priority
evaluator
timestamp
metadata
```

### 7.4 Field Descriptions

| Field                  | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `policy_evaluation_id` | Unique identifier for the policy evaluation.                                                   |
| `value_relation_id`    | Value Relation being evaluated.                                                                |
| `policy_profile`       | Policy profile or rule set used for evaluation.                                                |
| `evaluation_result`    | Result of the policy evaluation.                                                               |
| `boundary_flags`       | Boundaries triggered by the evaluation.                                                        |
| `required_actions`     | Follow-up actions required by the policy.                                                      |
| `review_priority`      | Priority level for review.                                                                     |
| `evaluator`            | AI system, human reviewer, policy engine, or governance process that performed the evaluation. |
| `timestamp`            | Time at which the evaluation occurred.                                                         |
| `metadata`             | Additional non-core information.                                                               |

### 7.5 Suggested Evaluation Results

```text
no_action
record_only
requires_review
requires_attribution_review
requires_governance_review
requires_risk_review
out_of_scope
insufficient_evidence
prohibited_automatic_claim
approved_for_next_stage
other
```

### 7.6 Suggested Boundary Flags

```text
low_confidence
high_impact
false_attribution_risk
trace_poisoning_risk
privacy_risk
legal_review_required
compensation_out_of_scope
human_review_required
automatic_decision_prohibited
other
```

### 7.7 Suggested Review Priority

```text
low
normal
high
critical
```

---

## 8. Record Type 5: Review Record

### 8.1 Definition

A Review Record stores the outcome of a human, governance, or accountable review process.

It is the final minimal record in the v0.1 lifecycle.

Review Records preserve the distinction between machine detection, policy evaluation, and accountable conclusion.

### 8.2 Examples

Examples of Review Records include:

* A reviewer confirms that a source was meaningfully referenced.
* A governance process rejects a weak reuse claim.
* A relation is accepted for attribution but not compensation.
* A trace is marked as false attribution.
* A relation is archived as non-actionable.
* A review is deferred due to insufficient evidence.

### 8.3 Minimal Fields

```text
review_record_id
policy_evaluation_id
reviewer
review_type
review_decision
review_notes
decision_scope
timestamp
appeal_allowed
metadata
```

### 8.4 Field Descriptions

| Field                  | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `review_record_id`     | Unique identifier for the review record.                       |
| `policy_evaluation_id` | Policy Evaluation being reviewed.                              |
| `reviewer`             | Human, governance body, accountable system, or review process. |
| `review_type`          | Type of review performed.                                      |
| `review_decision`      | Outcome of the review.                                         |
| `review_notes`         | Optional notes explaining the decision.                        |
| `decision_scope`       | Scope of the decision.                                         |
| `timestamp`            | Time at which the review was recorded.                         |
| `appeal_allowed`       | Whether the decision may be challenged or reopened.            |
| `metadata`             | Additional non-core information.                               |

### 8.5 Suggested Review Types

```text
human_review
ai_assisted_review
governance_review
legal_review
technical_review
risk_review
attribution_review
other
```

### 8.6 Suggested Review Decisions

```text
accepted
rejected
partially_accepted
requires_more_evidence
out_of_scope
archived
disputed
escalated
other
```

### 8.7 Suggested Decision Scope

```text
record_only
attribution
governance
risk_control
future_circulation
compensation_review
legal_review
repository_scope
system_scope
unknown
```

---

## 9. Relationship Between Records

The five record types are connected but should remain separable.

```text
Communication Event
    creates context for
Trace Event
    supports
Value Relation
    is evaluated by
Policy Evaluation
    is concluded or recorded by
Review Record
```

This separation allows different systems to operate at different layers.

For example:

* A logging system may only create Communication Events.
* A trace detector may only create Trace Events.
* Royalty OS may structure Value Relations.
* A Policy Engine may create Policy Evaluations.
* A governance process may create Review Records.

---

## 10. Minimal Record Graph

A minimal graph may look like this:

```text
communication_event: CE-001
        |
        v
trace_event: TE-001
        |
        v
value_relation: VR-001
        |
        v
policy_evaluation: PE-001
        |
        v
review_record: RR-001
```

A more complex graph may include multiple traces and relations:

```text
CE-001
 ├─ TE-001
 │   ├─ VR-001
 │   └─ VR-002
 └─ TE-002
     └─ VR-003
          └─ PE-001
              └─ RR-001
```

Communication Royalty OS should support both minimal and complex graphs.

---

## 11. Actor Model

Actors may include:

```text
user
human_reviewer
ai_agent
ai_model
system
document
repository
service
merchant
governance_body
policy_engine
gateway
unknown
```

Each actor should be represented with:

```text
actor_id
actor_type
display_name
reference
metadata
```

The `reference` field may point to a URI, repository path, model ID, document hash, service endpoint, or internal identifier.

---

## 12. Entity Model

Entities may include:

```text
document
prompt
response
summary
model_output
reasoning_structure
transaction
decision
policy
trace_record
value_graph
review_record
repository_file
external_reference
other
```

Entities should be referenced in a way that supports traceability without requiring unnecessary exposure of private content.

---

## 13. Privacy and Minimization

Communication Royalty OS should not become a universal surveillance layer.

The data model should follow these principles:

```text
Record only what is necessary.
Prefer references over raw content.
Prefer hashes or redacted pointers where possible.
Separate evidence from private content.
Support deletion, redaction, or restricted access where required.
Avoid storing sensitive information unless necessary for accountable review.
```

Traceability must be balanced with privacy.

---

## 14. Integrity and Security Considerations

Trace records may be attacked or manipulated.

Potential risks include:

* False attribution
* Trace poisoning
* Replay attacks
* Context hijacking
* Unauthorized reuse claims
* Manipulated confidence scores
* Fabricated references
* Excessive automated value claims

The data model should support fields for:

```text
risk_flags
evidence_reference
confidence
detection_method
review_required
boundary_flags
review_decision
```

These fields help prevent the system from treating unverified traces as settled truth.

---

## 15. Non-Goals

This data model does not define payment execution.

It does not define banking integration.

It does not automatically calculate royalties.

It does not automatically determine legal ownership.

It does not require that every communication creates compensation.

It does not treat every similarity as reuse.

It does not replace human review.

It does not replace agentic commerce protocols.

It defines minimal records for trace-based value relationship review.

---

## 16. v0.1 Implementation Boundary

The v0.1 implementation should focus on three core schemas first:

```text
1. communication-event.schema.json
2. trace-event.schema.json
3. value-relation.schema.json
```

Policy Evaluation and Review Record may be added after the first three records are stable.

Recommended first implementation sequence:

```text
schemas/communication-event.schema.json
schemas/trace-event.schema.json
schemas/value-relation.schema.json

examples/communication-event.example.yaml
examples/trace-event.example.yaml
examples/value-relation.example.yaml
```

This keeps the first implementation small and testable.

---

## 17. Example Minimal Flow

A minimal flow may be represented as:

```yaml
communication_event:
  communication_event_id: "CE-001"
  timestamp: "2026-06-06T00:00:00Z"
  source_actor:
    actor_id: "agent-a"
    actor_type: "ai_agent"
  target_actor:
    actor_id: "agent-b"
    actor_type: "ai_agent"
  communication_type: "summary"
  content_reference: "hash:example-summary"
  context_reference: "session:example-session"
  session_reference: "session:example-session"

trace_event:
  trace_event_id: "TE-001"
  communication_event_id: "CE-001"
  trace_type: "summary_reuse"
  detected_source:
    entity_id: "doc-001"
    entity_type: "document"
  detected_target:
    entity_id: "hash:example-summary"
    entity_type: "summary"
  detection_method: "semantic_similarity"
  confidence: "medium"

value_relation:
  value_relation_id: "VR-001"
  trace_event_id: "TE-001"
  relation_type: "summarized_by"
  source_entity:
    entity_id: "doc-001"
    entity_type: "document"
  target_entity:
    entity_id: "hash:example-summary"
    entity_type: "summary"
  contribution_type: "knowledge"
  contribution_scope: "session"
  strength: "moderate"
  status: "pending_policy_evaluation"
  review_required: true
```

This example is illustrative only.

Formal examples should be created separately under the `examples/` directory.

---

## 18. Summary

Communication Royalty OS requires a data model that can record communication-based value relationships without overclaiming ownership, compensation, or legal meaning.

The minimal data model consists of:

```text
Communication Event
Trace Event
Value Relation
Policy Evaluation
Review Record
```

Together, these records allow the system to move from communication to trace detection, from trace detection to value structuring, from value structuring to policy evaluation, and from policy evaluation to accountable review.

The key distinction remains:

```text
The system records and structures value relationships.
It does not automatically decide value.
```

This is the foundation for responsible trace-based value circulation in AI-agent communications.
