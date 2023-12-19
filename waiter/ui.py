from htmltools import HTMLDependency


def use_waiter() -> HTMLDependency:
    '''
    Programatically show and hide loading screens.
    Place this somewhere in the UI code of your shiny app.
    
    '''
    return HTMLDependency(
        name="waiter",
        version="1.0.0",
        source={"package": "waiter", "subdir": "srcjs"},
        script={"src": "waiter.js"},
    )
