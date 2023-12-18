# py-waiter

## Getting started

```bash
python -m venv venv
source venv/bin/activate

# Stable
pip install git+ssh://git@git.eoda.de/insertnamehere/py-waiter.git

# Dev version
pip install git+ssh://git@git.eoda.de/insertnamehere/py-waiter.git@dev
```

See [examples](examples), e. g. run [app.py](examples/app1/app.py)

## Development

First install [Poetry](https://python-poetry.org/), then run:

```bash
poetry install

poetry run pytest

poetry shell
```

Add dependencies:

```bash
poetry add shiny
```

Add dev dependencies:

```bash
poetry add isort@latest --group dev
```

Buid:

```bash
poetry build
```
