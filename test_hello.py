from hello import say_hello


def test_say_hello_default():
    assert say_hello() == "Hello, World!"


def test_say_hello_name():
    assert say_hello("DevOps") == "Hello, DevOps!"
