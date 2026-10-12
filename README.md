# Detection-as-Code SOC

## Implemented
- GitHub Actions detection test and deployment workflow
- Ten detection rules with sample events and unit tests
- EventBridge rules deployed in ap-south-1
- Three Step Functions SOAR triage skeletons with approval-required states
- Synthetic incident CSV and HTML dashboard
- Initial MITRE ATT&CK technique mapping layer

## Limitations
- EventBridge alert targets and end-to-end alert delivery are not verified.
- SOAR approval is a placeholder; no containment or remediation is executed.
- Dashboard metrics use synthetic demo data, not live incident telemetry.
- MITRE mappings are proposed and require analyst validation.
- Attack simulation was not run.

## Validation
Run `python -m unittest discover -s tests -v` and validate JSON files with `python -m json.tool`.
