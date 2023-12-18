from waiter import spinners


def test_spinner_1():
    assert (
        spinners.spin_1()
        == "<div class='container--box'><div class='boxxy'><div class='spinner spinner--1'></div></div></div>"
    )
