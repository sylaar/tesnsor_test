from Script1 import test_sbis1
from conftest import driver


def test_1():
    assert (test_sbis1(driver))[0] == 'Сила в людях'

def test_2():
    assert (test_sbis1(driver))[1] == 'https://tensor.ru/about'

def test_3():
    assert (test_sbis1(driver))[2] == True
