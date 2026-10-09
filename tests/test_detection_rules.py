import json
import unittest
from pathlib import Path

import yaml

from scripts.detection_engine import matches_rule

ROOT = Path(__file__).resolve().parents[1]


class RootLoginDetectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / "rules/root-console-login.yaml").open() as file:
            cls.rule = yaml.safe_load(file)

    def load_event(self, path):
        with (ROOT / path).open() as file:
            return json.load(file)

    def test_successful_root_login_should_match(self):
        event = self.load_event(
            "samples/positive/root-console-login.json"
        )
        self.assertTrue(matches_rule(event, self.rule))

    def test_iam_user_login_should_not_match(self):
        event = self.load_event(
            "samples/negative/iam-user-login.json"
        )
        self.assertFalse(matches_rule(event, self.rule))

    def test_rule_metadata(self):
        self.assertEqual(self.rule["severity"], "high")
        self.assertEqual(self.rule["attack"]["technique"], "T1078")
        self.assertTrue(self.rule["enabled"])


if __name__ == "__main__":
    unittest.main()
