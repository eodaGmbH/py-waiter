import time

from shiny import App, render, ui
from waiter import use_waiter, waiter_show

app_ui = ui.page_fluid(
    use_waiter(),
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt", placeholder=True),
)


def server(input, output, session):
    @render.text
    async def txt():
        await waiter_show("txt")
        time.sleep(5)
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
