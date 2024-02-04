from SbisPage3 import SbisScript3
from selenium import webdriver
from SbisPage2 import SbisLocators


def test_sbis3(driver) -> list[str, str, bool, str, str]:
    '''Конкретный сценарий тестирования'''
    result = []
    sbis_main_page = SbisScript3('https://sbis.ru')
    sbis_main_page.go_to_site()
    sbis_main_page.go_to_download_sbis()
    sbis_main_page.go_to_sbis_plugin()
    result.append(sbis_main_page.download_web_installer())
    return result

if __name__ == '__main__':
    test_sbis3(webdriver.Chrome())