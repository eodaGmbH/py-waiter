from shiny.session import get_current_session

from .spinners import spin_1


async def waiter_show(id_=None, html=spin_1(), color="black"):
    session = get_current_session()
    opts = {"id": id_, "html": html, "color": color}
    await session.send_custom_message("waiter-show", opts)


async def waiter_hide(id_=None):
    session = get_current_session()
    await session.send_custom_message("waiter-hide", {"id": id_})
