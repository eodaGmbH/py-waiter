from htmltools import HTMLDependency


def use_waiter() -> HTMLDependency:
    return HTMLDependency(
        name="waiter",
        version="1.0.0",
        source={"package": "waiter", "subdir": "srcjs"},
        script={"src": "waiter.js"},
    )
