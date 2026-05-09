def run_checks(data):
    findings = []

    # S3 checks
    for bucket in data.get("s3_buckets", []):
        if bucket.get("public"):
            findings.append({
                "resource": bucket["name"],
                "severity": "High",
                "issue": "Public S3 bucket"
            })

        if not bucket.get("encrypted"):
            findings.append({
                "resource": bucket["name"],
                "severity": "High",
                "issue": "Encryption disabled"
            })

        if not bucket.get("versioning"):
            findings.append({
                "resource": bucket["name"],
                "severity": "Medium",
                "issue": "Versioning disabled"
            })

    # Security group checks
    for sg in data.get("security_groups", []):
        for rule in sg.get("inbound", []):
            if rule.get("port") == 22 and rule.get("source") == "0.0.0.0/0":
                findings.append({
                    "resource": sg["name"],
                    "severity": "High",
                    "issue": "SSH open to the internet"
                })

    # IAM checks
    for user in data.get("iam_users", []):
        if "AdministratorAccess" in user.get("policies", []):
            findings.append({
                "resource": user["name"],
                "severity": "Medium",
                "issue": "AdministratorAccess policy attached"
            })

    return findings