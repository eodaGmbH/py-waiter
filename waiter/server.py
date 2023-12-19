from shiny.session import get_current_session

from .spinners import spin_1


async def waiter_show(
    id_: str = None, html: str = spin_1(), color: str = "black"
) -> None:
    """Show waiting screen."""
    session = get_current_session()
    opts = {"id": id_, "html": html, "color": color}
    await session.send_custom_message("waiter-show", opts)


async def waiter_hide(id_: str = None) -> None:
    """Hide waiting screen."""
    session = get_current_session()
    await session.send_custom_message("waiter-hide", {"id": id_})
