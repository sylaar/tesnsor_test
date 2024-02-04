from Script2 import test_sbis2
from conftest import driver


def test_1():
    assert (test_sbis2(driver))[0] == 'Ярославская обл.'

def test_2():
    assert (test_sbis2(driver))[1].find('Ярославль') != -1

def test_3():
    assert (test_sbis2(driver))[2] != (-1, -1)

def test_4():
    assert (test_sbis2(driver))[3] == 'Камчатский край'

def test_5():
    assert (test_sbis2(driver))[4].find('Камчатский') != -1