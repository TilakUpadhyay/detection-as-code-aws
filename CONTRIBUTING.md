# Contributing

Thanks for your interest in contributing! Please follow these steps:

## Development Environment

- Python 3.11+
- Create a virtual environment and install the project in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
```

## Commit Style

- Use clear, descriptive commit messages
- Prefer small, focused PRs
- Add or update unit tests where applicable

## Running Tests

```bash
pytest -q
```

## Code Style

- Follow the existing formatting and the repository's code style
- Avoid large refactors unrelated to the change

## Reporting Issues / Feature Requests

- Open a GitHub issue with reproduction steps or proposal details

## Security

If you discover a security issue, please do not open a public issue. Email the maintainers privately. 