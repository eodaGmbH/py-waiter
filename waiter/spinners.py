def construct_spinner(class_names) -> str:
    return (
        "".join([f"<div class='{cn}'>" for cn in class_names])
        + len(class_names) * "</div>"
    )


def spin_n(n=1) -> str:
    class_names = ["container--box", "boxxy", f"spinner spinner--{n}"]
    return construct_spinner(class_names)


def spin_1() -> str:
    return spin_n(1)


def spin_2() -> str:
    return spin_n(2)


def spin_double_bounce() -> str:
    class_names = ["double-bouncer", "double-bounce1", "double-bounce2"]
    return construct_spinner(class_names)


def spin_rotating_plane() -> str:
    return construct_spinner(["rotating-plane"])


def spin_wave() -> str:
    class_names = ["waver", "rect1", "rect2", "rect3"]
    return construct_spinner(class_names)
