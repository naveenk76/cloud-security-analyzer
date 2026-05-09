Cloud Security Analyzer

A Python project that analyzes a sample cloud architecture file and identifies common security misconfigurations in storage, networking, and IAM.

What It Checks

The tool looks for issues such as:
-Public S3 buckets
-Buckets without encryption
-Versioning disabled
-SSH (port 22) open to 0.0.0.0/0
-IAM users with AdministratorAccess


Project Structure
cloud-security-analyzer/
├── main.py
├── checks.py
├── sample_architecture.json
├── report.json
├── requirements.txt
└── README.md
How to Run
Create and activate a virtual environment.
Install dependencies:
pip install -r requirements.txt
Run the script:
python main.py
Output

The script generates a report.json file containing all findings with severity levels.

Example:
JSON:
[
  {
    "resource": "customer-data",
    "severity": "High",
    "issue": "Public S3 bucket"
  }
]


Sample Input

The project reads data from sample_architecture.json, which contains a simplified cloud environment description.
