def construct_spinner(class_names):
    return (
        "".join([f"<div class='{cn}'>" for cn in class_names])
        + len(class_names) * "</div>"
    )


def spin_n(n=1):
    class_names = ["container--box", "boxxy", f"spinner spinner--{n}"]
    return construct_spinner(class_names)


def spin_1():
    return spin_n(1)


def spin_2():
    return spin_n(2)


def spin_double_bounce():
    class_names = ["double-bouncer", "double-bounce1", "double-bounce2"]
    return construct_spinner(class_names)
