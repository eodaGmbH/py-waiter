from waiter import use_waiter


def test_use_waiter():
    dep = use_waiter()
    print(dep)

    assert dep.name == "waiter"
