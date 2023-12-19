# py-waiter

## Getting started

This repository provides a py-shiny implementation of the [waiter package from John Coene](https://github.com/JohnCoene/waiter). 
The waiter package allows the usage of loading screens and spinners in [shiny applications](https://shiny.posit.co/).

### Installation

```bash
python -m venv venv
source venv/bin/activate

# Stable
pip install git+https://github.com/eodaGmbH/py-waiter@main

# Dev version
pip install git+https://github.com/eodaGmbH/py-waiter@dev
```

### Usage

```python
import time

from shiny import App, render, ui
from waiter import use_waiter, waiter_show
from waiter.spinners import spin_1

app_ui = ui.page_fluid(
    use_waiter(), # include dependencies
    ui.output_text_verbatim("txt", placeholder=True)
    # ...
)

def server(input, output, session):
    @render.text
    async def txt():
        await waiter_show("txt", html=spin_1()) # show spinner 1
        time.sleep(5)
        return "Hello Spinner!"
```

## Examples

* [app1](examples/app1/app.py)
* [app2](examples/app2/app.py)

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

Build:

```bash
poetry build
```
