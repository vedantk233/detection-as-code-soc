# Detection-as-Code SOC

A Git-managed detection engineering project with automated testing,
deployment workflows, SOAR playbooks, attack simulation, and MITRE
ATT&CK coverage.

## Current capabilities
- YAML-based detection rule for successful AWS root console logins.
- Positive and negative sample CloudTrail-style events.
- Python detection evaluation logic.
- Automated unit tests using Python unittest.
- GitHub Actions workflow for pushes and pull requests.

## Run locally
Install dependencies:
    python -m pip install -r requirements.txt

Run tests:
    python -m unittest discover -s tests -v

## Project structure
- `rules/` — YAML detection rules
- `samples/positive/` — Events expected to match
- `samples/negative/` — Events expected not to match
- `scripts/` — Detection evaluation and deployment utilities
- `tests/` — Automated tests
- `deploy/` — Deployment configuration
- `.github/workflows/` — CI workflows
- `docs/` — Architecture and project documentation
