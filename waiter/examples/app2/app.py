import time

from shiny import App, render, ui

from waiter import use_waiter, waiter_hide, waiter_show
from waiter.spinners import spin_double_bounce, spin_rotating_plane, spin_wave

app_ui = ui.page_fluid(
    use_waiter(),
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt", placeholder=True),
)


def server(input, output, session):
    @render.text
    async def txt():
        await waiter_show(html=spin_wave())
        time.sleep(3)
        await waiter_hide()
        await waiter_show(html=spin_double_bounce())
        time.sleep(3)
        await waiter_hide()
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
