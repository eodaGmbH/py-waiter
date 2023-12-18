# py-waiter

## Getting started

```bash
pip install git+ssh://git@git.eoda.de/insertnamehere/py-waiter.git

# Dev version
pip install git+ssh://git@git.eoda.de/insertnamehere/py-waiter.git@dev
```

### With Poetry

First install [Poetry](https://python-poetry.org/), then run:

```bash
poetry install

poetry run pytest

poetry shell
```

### Without Poetry

```bash
python -m venv venv
source venv/bin/activate
pip install .
```

## Development

Add dependencies:

```bash
poetry add shiny
```

Add dev dependencies:

```bash
poetry add isort@latest --group dev
```
