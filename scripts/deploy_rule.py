import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from convert_rule import convert_rule


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/deploy_rule.py <rule.yaml>")
        sys.exit(2)

    rule_path = Path(sys.argv[1])

    with rule_path.open() as file:
        rule = yaml.safe_load(file)

    if not rule.get("enabled", True):
        print(f"Skipping disabled rule: {rule['name']}")
        return

    pattern = convert_rule(rule)
    rule_name = f"detection-{rule['name']}"

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False
    ) as temp:
        json.dump(pattern, temp, indent=2)
        pattern_path = temp.name

    try:
        command = [
            "aws", "events", "put-rule",
            "--name", rule_name,
            "--description", rule.get("description", rule_name),
            "--event-pattern", f"file://{pattern_path}",
            "--state", "ENABLED",
            "--event-bus-name", "default",
        ]

        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Deployed: {rule_name}")
        print(result.stdout)
    finally:
        Path(pattern_path).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
