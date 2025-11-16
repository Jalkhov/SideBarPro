from unittest import defaultTestLoader


def all_tests():
    return defaultTestLoader.discover("tests", pattern="test*.py")
