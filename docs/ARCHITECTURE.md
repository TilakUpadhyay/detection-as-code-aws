# Architecture

This project compiles a single detection definition (YAML/JSON) into multiple AWS backend queries using a simple pipeline.

## Components

- Rule Schema: `title`, `id`, `description`, `logsource`, `detection.condition`, `output` flags
- Parser: Loads YAML/JSON into `Rule` dataclass (`detectc/models.py`, `detectc/parser.py`)
- IR (Intermediate Representation): The `Rule` object; future versions can add normalized fields
- Compilers: Target-specific compilers translate the condition and render templates
  - CloudWatch Logs Insights (`detectc/compiler/cloudwatch.py`)
  - Athena SQL (`detectc/compiler/athena.py`)
  - Security Hub Insight JSON (`detectc/compiler/securityhub.py`)
- Templates: Jinja2 templates per backend under `detectc/compiler/templates/*`
- CLI: `detectc compile <rule> --targets ... --out ...`

## Flow

1. Read YAML/JSON rule and validate required fields
2. Translate the pseudo-condition to a target-specific expression
3. Render Jinja2 template with rule context and translated condition
4. Write compiled query artifact(s) to disk

## Condition Translator

For v0.1 a minimal translator maps basic boolean/equals to backend syntax. Future versions can add:

- Proper expression grammar (lexer/parser)
- Field mapping per log source (e.g., CloudTrail vs ALB vs S3 access logs)
- Normalization to OCSF or custom schema

## Security Hub Insights

Security Hub insights use filters and group-by attributes. In v0.1, we store the condition in `NoteText` as a hint; future work includes mapping to structured filters when possible. 