from waiter import spinners

def test_construct_spinners():
    # Prepare
    class_names = [
        "container--box",
        "boxxy",
        "spinner spinner--1"
    ]

    # Act
    html = spinners.construct_spinner(class_names)

    # Assert
    assert html == "<div class='container--box'><div class='boxxy'><div class='spinner spinner--1'></div></div></div>"
def test_spinner_1():
    # Assert
    assert (
        spinners.spin_1()
        == "<div class='container--box'><div class='boxxy'><div class='spinner spinner--1'></div></div></div>"
    )
