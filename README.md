# Detection-as-Code for AWS
[![CI](https://github.com/TilakUpadhyay/detection-as-code-aws/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ABCD/detection-as-code-aws/actions/workflows/ci.yml)

A modular framework that lets analysts author portable detections in YAML/JSON and compile them to multiple AWS backends:

- CloudWatch Logs Insights queries
- Amazon Athena SQL (for S3 log analysis)
- AWS Security Hub custom insights

## Why

Detection portability across AWS log sources and tools is hard. This project introduces a simple, opinionated schema and compilers that translate a single detection definition into multiple query targets.

## Status

Early scaffold. CLI and compilers are being implemented. See `docs/` for design and roadmap once available.

## Features

- Rule authoring in YAML/JSON
- CLI `detectc` compiles rules to targets
- Modular compilers (CloudWatch, Athena, Security Hub)
- Jinja2-based templates for consistent output
- Pytest tests (coming soon)

## Quickstart

```bash
# Requires Python 3.11+
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .

# Compile a detection (examples to be added)
detectc compile detections/s3_access_anomaly.yaml --targets cloudwatch athena securityhub --out examples/
```

## Repository Layout

```
detection-as-code-aws/
├── detections/        # Sample YAML/JSON detection rules
├── compiler/          # Scripts to convert rules into queries
│   ├── cloudwatch/
│   ├── athena/
│   └── securityhub/
├── examples/          # Example compiled queries
├── docs/              # Documentation & usage guides
├── tests/             # Unit tests
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing

See `CONTRIBUTING.md` for guidance on setting up your development environment and submitting changes. 
