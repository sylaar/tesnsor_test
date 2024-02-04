from SbisPage1 import SbisScript1
from selenium import webdriver


def test_sbis1(driver) -> list[str, str, bool]:
    '''Конкретный сценарий тестирования'''
    result = []
    sbis_main_page = SbisScript1('https://sbis.ru')
    sbis_main_page.go_to_site()
    sbis_main_page.go_to_sbis_contacts()
    sbis_main_page.go_to_tenzor_banner()
    result.append(sbis_main_page.check_existance_block())
    sbis_main_page.go_to_tensor_detail()
    result.append(sbis_main_page.get_current_url())
    result.append(sbis_main_page.check_images())
    return result
    

if __name__ == '__main__':
    test_sbis1(webdriver.Chrome())