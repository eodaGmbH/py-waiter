from htmltools import HTMLDependency


def use_waiter() -> HTMLDependency:
    """Add waiter dependencies. Include it anywhere in your UI but ideally at the top."""
    return HTMLDependency(
        name="waiter",
        version="1.0.0",
        source={"package": "waiter", "subdir": "srcjs"},
        script={"src": "waiter.js"},
    )
