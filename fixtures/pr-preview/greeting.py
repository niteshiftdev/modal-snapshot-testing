"""Tiny module the seeded review guide points at."""


def greeting(name: str) -> str:
    """Return a friendly greeting for `name`."""
    trimmed = name.strip()
    if not trimmed:
        return "Hello, stranger!"
    return f"Hello, {trimmed}!"


def shout(name: str) -> str:
    """Return the greeting in upper case."""
    return greeting(name).upper()
