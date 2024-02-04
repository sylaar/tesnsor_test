from Script3 import test_sbis3
from conftest import driver


def test_1():
    assert (test_sbis3(driver))[0] == 7.36