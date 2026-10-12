# Final Project Status

## Implemented
- GitHub Actions detection test and deployment workflow
- Ten EventBridge detection rules and sample unit tests
- Three Step Functions SOAR triage skeletons
- Synthetic incident CSV and HTML dashboard
- Initial MITRE ATT&CK mapping JSON

## Pending Validation / Work
- Verify all ten detections match the capstone-required scenarios
- Add tuning, allow-lists, false-positive estimates, correlation and enrichment
- Implement task-token human approval, evidence collection, notification and safe containment
- Run approved simulations in a dedicated sandbox; record detection/playbook outcomes and cleanup
- Connect case timestamps and calculate real MTTD/MTTR
- Add 15-minute high-severity acknowledgement alarm
- Validate ATT&CK mappings, document top three gaps and quarterly purple-team plan
- Complete architecture/playbook diagrams, demo dry-run and final teardown
