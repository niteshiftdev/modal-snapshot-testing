from greeting import greeting, shout


def test_greeting_trims_whitespace():
    assert greeting("  Ada ") == "Hello, Ada!"


def test_greeting_handles_empty_name():
    assert greeting("   ") == "Hello, stranger!"


def test_shout_upper_cases():
    assert shout("Ada") == "HELLO, ADA!"
