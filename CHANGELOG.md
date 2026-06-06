# Changelog

All notable changes to this project will be documented in this file.

This project follows a draft-first specification workflow.
Current entries are organized under `[Unreleased]` until a release tag is created.

---

## [Unreleased]

### Added

* Added `docs/communication-royalty-os-architecture.md`.

  * Defines Communication Royalty OS as an upper-layer architecture for trace-based value circulation in AI-agent communications.
  * Clarifies the relationship between Communication Royalty OS, Royalty OS, Trace Protocol, Agentic Commerce, and gateway/defense layers.
  * Establishes Communication Royalty OS as a communication-value relationship layer rather than a payment execution layer.
  * Defines non-goals to avoid replacing payment protocols, banking infrastructure, legal ownership systems, or agentic commerce standards.

* Added `docs/communication-royalty-os-data-model.md`.

  * Defines the minimal data model for Communication Royalty OS.
  * Introduces five core record types:

    * Communication Event
    * Trace Event
    * Value Relation
    * Policy Evaluation
    * Review Record
  * Establishes the minimal lifecycle from communication to trace detection, value structuring, policy evaluation, and accountable review.
  * Clarifies the core principle:

    * Detection is not attribution.
    * Attribution is not compensation.
    * Compensation is not automatic.

* Added core JSON Schemas.

  * Added `schemas/communication-event.schema.json`.
  * Added `schemas/trace-event.schema.json`.
  * Added `schemas/value-relation.schema.json`.
  * Added `schemas/policy-evaluation.schema.json`.
  * Added `schemas/review-record.schema.json`.

* Added core YAML examples.

  * Added `examples/communication-event.example.yaml`.
  * Added `examples/trace-event.example.yaml`.
  * Added `examples/value-relation.example.yaml`.
  * Added `examples/policy-evaluation.example.yaml`.
  * Added `examples/review-record.example.yaml`.

* Added local validation support.

  * Added `scripts/validate_examples.py`.
  * Validates example YAML files against their corresponding JSON Schema definitions.
  * Supports the full five-stage Communication Royalty OS lifecycle.

* Added GitHub Actions validation workflow.

  * Added `.github/workflows/validate-examples.yml`.
  * Runs schema/example validation automatically on `push` to `main`.
  * Runs validation automatically on `pull_request`.

* Added README documentation for the full core lifecycle.

  * Added project overview.
  * Added core thesis.
  * Added design principles.
  * Added key documents.
  * Added core schemas.
  * Added example records.
  * Added record lifecycle explanation.
  * Added relationship to Agentic Commerce.
  * Added relationship to Royalty OS and Trace Protocol.
  * Added repository structure.
  * Added validation instructions.
  * Added GitHub Actions section.
  * Added current v0.1 scope.
  * Added non-goals.
  * Added future extensions.
  * Added development workflow.

### Changed

* Expanded the project from an architecture-only draft into a machine-checkable validation package.
* Updated the repository structure to include:

  * `docs/`
  * `schemas/`
  * `examples/`
  * `scripts/`
  * `.github/workflows/`
* Updated validation coverage from three core records to the full five-record lifecycle:

  * Communication Event
  * Trace Event
  * Value Relation
  * Policy Evaluation
  * Review Record

### Validation

* Confirmed that the full validation flow passes with:

```bash
python scripts/validate_examples.py
```

* Current validated schema/example pairs:

```text
schemas/communication-event.schema.json
  -> examples/communication-event.example.yaml

schemas/trace-event.schema.json
  -> examples/trace-event.example.yaml

schemas/value-relation.schema.json
  -> examples/value-relation.example.yaml

schemas/policy-evaluation.schema.json
  -> examples/policy-evaluation.example.yaml

schemas/review-record.schema.json
  -> examples/review-record.example.yaml
```

### Notes

* Communication Royalty OS remains a draft specification.
* The current version does not implement payment execution, banking integration, automatic royalty calculation, legal ownership determination, or automatic attribution enforcement.
* The current focus is to define a minimal, reviewable, and machine-checkable foundation for trace-based value circulation in AI-agent communications.

---

## Release Planning

### Candidate: v0.1.0-candidate

The current repository state is suitable for a future `v0.1.0-candidate` release once the following checks are complete:

* README reviewed.
* CHANGELOG reviewed.
* All examples pass validation.
* GitHub Actions passes on `main`.
* Repository files are committed.
* Release tag is prepared.

Recommended future tag:

```text
v0.1.0-candidate
```

Recommended release title:

```text
Communication Royalty OS v0.1.0-candidate
```
