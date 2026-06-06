#!/usr/bin/env python3
"""
Validate Communication Royalty OS example YAML files against JSON Schema files.

Required packages:
- PyYAML
- jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path

# -----------------------------
# Safe imports
# -----------------------------
try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    raise SystemExit(1) from exc

# -----------------------------
# Paths
# -----------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    {
        "name": "Communication Event",
        "schema": REPO_ROOT / "schemas" / "communication-event.schema.json",
        "example": REPO_ROOT / "examples" / "communication-event.example.yaml",
    },
    {
        "name": "Trace Event",
        "schema": REPO_ROOT / "schemas" / "trace-event.schema.json",
        "example": REPO_ROOT / "examples" / "trace-event.example.yaml",
    },
    {
        "name": "Value Relation",
        "schema": REPO_ROOT / "schemas" / "value-relation.schema.json",
        "example": REPO_ROOT / "examples" / "value-relation.example.yaml",
    },
]

# -----------------------------
# Loaders
# -----------------------------
def load_json(path: Path) -> dict:
    """Load a JSON file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}") from None
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc

    if data is None:
        raise RuntimeError(f"YAML file is empty: {path}")

    if not isinstance(data, dict):
        raise RuntimeError(f"YAML root must be an object/map: {path}")

    return data


# -----------------------------
# Error formatting
# -----------------------------
def format_validation_path(error: ValidationError) -> str:
    """Format a jsonschema validation error path."""
    if not error.absolute_path:
        return "<root>"
    return ".".join(str(part) for part in error.absolute_path)


# -----------------------------
# Validation logic
# -----------------------------
def validate_target(name: str, schema_path: Path, example_path: Path) -> None:
    """Validate one example file against one schema file."""
    print(f"Validating target: {name}")
    print(f"  Schema:  {schema_path.relative_to(REPO_ROOT)}")
    print(f"  Example: {example_path.relative_to(REPO_ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"Invalid schema in {schema_path}: {exc.message}") from exc

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda err: list(err.absolute_path))

    if errors:
        print("")
        print(f"Validation failed for target: {name}")

        for error in errors:
            path = format_validation_path(error)
            print(f"  - Path: {path}")
            print(f"    Error: {error.message}")

        raise RuntimeError(f"{name} example failed validation.")

    print(f"  Result: passed\n")


# -----------------------------
# Main
# -----------------------------
def main() -> int:
    """Run all validations."""
    print("Communication Royalty OS example validation\n")

    try:
        for target in TARGETS:
            validate_target(
                name=target["name"],
                schema_path=target["schema"],
                example_path=target["example"],
            )
    except RuntimeError as exc:
        print("\nValidation failed.")
        print(exc)
        return 1

    print("All examples passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

