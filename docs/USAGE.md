# Usage

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Author a Detection

Create a YAML file under `detections/`:

```yaml
title: S3 Suspicious Access
id: s3_access_anomaly
description: Detects unusual S3 GetObject activity from uncommon IPs.
logsource: s3_access_logs
detection:
  condition: eventName == "GetObject" and not ipAddress in known_ips
output:
  cloudwatch: true
  athena: true
  securityhub: true
```

## Compile

```bash
detectc compile detections/s3_access_anomaly.yaml --targets cloudwatch athena securityhub --out examples/
```

Outputs will be written to `examples/`:

- `s3_access_anomaly.cloudwatch.insights`
- `s3_access_anomaly.athena.sql`
- `s3_access_anomaly.securityhub.json`

## Notes

- The condition language is a minimal pseudo-expression and is translated per backend. Future versions will add a proper expression grammar.
- `logsource` is used as the Athena table name and as context for other backends. Map it to your environment as needed. 