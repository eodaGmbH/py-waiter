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


def spin_wandering_cubes() -> str:
    class_names = ["wandering-cubes", "cube1", "cube2"]
    return construct_spinner(class_names)


def spin_pulse() -> str:
    return construct_spinner(["pulser"])


def spin_chasing_dots() -> str:
    class_names = ["chasing-dots", "dot1", "dot2"]
    return construct_spinner(class_names)


def spin_three_bounce() -> str:
    class_names = ["three-bouncer", "bounce1", "bounce2", "bounce3"]
