# Contributing

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest ruff
```

## Validate before PR

```bash
make lint
make test
```

## Standards

- Keep each project independently runnable.
- Add tests for algorithmic helpers when changing behavior.
- Update README/docs when changing commands or ports.
