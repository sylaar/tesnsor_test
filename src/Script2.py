from SbisPage2 import SbisScript2
from selenium import webdriver
from SbisPage2 import SbisLocators


def test_sbis2(driver) -> list[str, str, bool, str, str]:
    '''Конкретный сценарий тестирования'''
    result = []
    sbis_main_page = SbisScript2('https://sbis.ru')
    sbis_main_page.go_to_site()
    sbis_main_page.go_to_sbis_contacts()
    result.append(sbis_main_page.check_region(SbisLocators.LOCATOR_SBIS_CONTACTS_REGION))
    result.append(sbis_main_page.search_partners_list(SbisLocators.LOCATOR_SBIS_PARTNERS))
    sbis_main_page.choose_region()
    result.append(sbis_main_page.check_new_region())
    result.append(sbis_main_page.check_region(SbisLocators.LOCATOR_SBIS_CONTACTS_REGION))
    result.append(sbis_main_page.search_partners_list(SbisLocators.LOCATOR_SBIS_PARTNERS))
    return result


if __name__ == '__main__':
    test_sbis2(webdriver.Chrome())