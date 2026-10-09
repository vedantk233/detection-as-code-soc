import json
import sys
from pathlib import Path

import yaml

FIELD_MAP = {
    "event_source": ["eventSource"],
    "event_name": ["eventName"],
    "user_type": ["userIdentity", "type"],
    "response_elements": ["responseElements"],
}


def convert_rule(rule):
    detail = {}

    for key, value in rule.get("query", {}).items():
        if key not in FIELD_MAP:
            raise ValueError(f"Unsupported query field: {key}")

        path = FIELD_MAP[key]
        current = detail

        for field in path[:-1]:
            current = current.setdefault(field, {})

        current[path[-1]] = value

    return {
        "source": ["aws.signin"],
        "detail-type": ["AWS Console Sign In via CloudTrail"],
        "detail": detail,
    }


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python scripts/convert_rule.py "
            "<input.yaml> <output.json>"
        )
        sys.exit(2)

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])

    with source.open() as file:
        rule = yaml.safe_load(file)

    pattern = convert_rule(rule)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(pattern, indent=2) + "\n")
    print(f"Converted {source} -> {destination}")


if __name__ == "__main__":
    main()
