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


def spin_rotating_plane() -> str:
    return construct_spinner(["rotating-plane"])


def spin_fading_circles() -> str:
    class_names = [
        "sk-fading-circle",
        "sk-circle1 sk-circle",
        "sk-circle2 sk-circle",
        "sk-circle3 sk-circle",
        "sk-circle4 sk-circle",
        "sk-circle5 sk-circle",
        "sk-circle6 sk-circle",
        "sk-circle7 sk-circle",
        "sk-circle8 sk-circle",
        "sk-circle9 sk-circle",
        "sk-circle10 sk-circle",
        "sk-circle11 sk-circle",
        "sk-circle12 sk-circle",
    ]
    return construct_spinner(class_names)


def spin_folding_cube() -> str:
    class_names = [
        "sk-folding-cube",
        "sk-cube1 sk-cube",
        "sk-cube2 sk-cube",
        "sk-cube3 sk-cube",
        "sk-cube4 sk-cube",
    ]
    return construct_spinner(class_names)


def spin_double_bounce() -> str:
    class_names = ["double-bouncer", "double-bounce1", "double-bounce2"]
    return construct_spinner(class_names)


def spin_wave() -> str:
    class_names = ["waver", "rect1", "rect2", "rect3", "rect4", "rect5"]
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


def spin_circle() -> str:
    class_names = [
        "sk-circle",
        "sk-circle1 sk-child",
        "sk-circle2 sk-child",
        "sk-circle3 sk-child",
        "sk-circle4 sk-child",
        "sk-circle5 sk-child",
        "sk-circle6 sk-child",
        "sk-circle7 sk-child",
        "sk-circle8 sk-child",
        "sk-circle9 sk-child",
        "sk-circle10 sk-child",
        "sk-circle11 sk-child",
        "sk-circle12 sk-child",
    ]
    return construct_spinner(class_names)

def spin_rotate() -> str:
    class_names = [
        "spinner-box","circle-border","circle-core"
    ]
    return construct_spinner(class_names)

def spin_solar() -> str:
    class_names = [
        "spinner-box", "earth-orbit orbit", "planet earth", "venus-orbit orbit",
        "planet venus", "mercury-orbit orbit", "planet mercury", "sun"
    ]
    return construct_spinner(class_names)

def spin_orbit() -> str:
    class_names = [
        "spinner-box", "blue-orbit leo","green-orbit leo","red-orbit leo",
        "white-orbit w1 leo",
        "white-orbit w2 leo","white-orbit w3 leo"
    ]
    return construct_spinner(class_names)

def spin_squares() -> str:
    class_names = [
        "spinner-box", "configure-border-1", "configure-core", "configure-border-2", "configure-core"
    ]
    return construct_spinner(class_names)

def spin_cube_grid() -> str:
    class_names =[
        "sk-cube-grid","sk-cube sk-cube1","sk-cube sk-cube2","sk-cube sk-cube3","sk-cube sk-cube4",
        "sk-cube sk-cube5","sk-cube sk-cube6","sk-cube sk-cube7","sk-cube sk-cube8","sk-cube sk-cube9"
    ]
    return construct_spinner(class_names)

#def spin_circles() -> str:
#    return construct_spinner("lds-circle")

def spin_orbiter() -> str:
    class_names = [
        "orbiter-spinner", "orbiter", "orbiter", "orbiter"
    ]
    return construct_spinner(class_names)
    
def spin_pixel() -> str:
    return construct_spinner(["pixel-spinner", "pixel-spinner-inner"])

def spin_flower() -> str:
    class_names = ["flower-spinner", "dots-container", "bigger-dot", "smaller-dot"]
    return construct_spinner(class_names)