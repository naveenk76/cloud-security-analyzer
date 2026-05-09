import json
from checks import run_checks

with open("sample_architecture.json", "r") as f:
    architecture = json.load(f)

findings = run_checks(architecture)

with open("report.json", "w") as f:
    json.dump(findings, f, indent=4)

print("Analysis complete. Report saved to report.json")