import json
import unittest
from pathlib import Path
import yaml
from scripts.detection_engine import matches_rule

class AdditionalDetectionTests(unittest.TestCase):
    def test_all_additional_rules_positive_and_negative(self):
        for path in sorted(Path("rules").glob("*.yaml")):
            with self.subTest(rule=path.name):
                rule = yaml.safe_load(path.read_text())
                if rule["name"] == "root-console-login":
                    continue
                name = rule["name"]
                positive = json.loads(Path("samples/positive", f"{name}.json").read_text())
                negative = json.loads(Path("samples/negative", f"{name}.json").read_text())
                self.assertTrue(matches_rule(positive, rule))
                self.assertFalse(matches_rule(negative, rule))

if __name__ == "__main__":
    unittest.main()
