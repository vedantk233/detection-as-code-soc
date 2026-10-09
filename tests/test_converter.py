import unittest
import yaml
from pathlib import Path

from scripts.convert_rule import convert_rule

ROOT = Path(__file__).resolve().parents[1]


class ConverterTests(unittest.TestCase):
    def test_eventbridge_pattern_structure(self):
        with (ROOT / "rules/root-console-login.yaml").open() as f:
            rule = yaml.safe_load(f)

        pattern = convert_rule(rule)

        self.assertIn("source", pattern)
        self.assertIn("detail-type", pattern)
        self.assertIn("eventSource", pattern["detail"])
        self.assertNotIn("detail", pattern["detail"])
        self.assertEqual(
            pattern["detail"]["userIdentity"]["type"], ["Root"]
        )


if __name__ == "__main__":
    unittest.main()
