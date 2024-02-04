from BasePage import BasePage
from selenium.webdriver.common.by import By


class SbisLocators:
    '''Задает локатары для конкретного сценария'''
    LOCATOR_SBIS_CONTACTS_PAGE = (By.CSS_SELECTOR, 'li.sbisru-Header__menu-item:nth-child(2) > a:nth-child(1)')
    LOCATOR_SBIS_TENSOR_BANNER = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm > a:nth-child(1) > img:nth-child(1)')
    LOCATOR_TENSOR_BLOCK_PEOPLE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:nth-child(1)')
    LOCATOR_TENSOR_DETAIL = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:nth-child(4) > a:nth-child(1)')
    LOCATOR_TENSOR_IMG_BY_TEXT = (By.CSS_SELECTOR, 'div.tensor_ru-container:nth-child(4)')    

class SbisScript1(BasePage):
    '''Класс сценария тестирования'''

    def go_to_sbis_contacts(self):
        '''Переход на https://sbis/contacts'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_CONTACTS_PAGE)
        search_field.click()
        return search_field
    

    def go_to_tenzor_banner(self):
        '''Поиск баннера Тензор и клик по нему'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_TENSOR_BANNER)
        search_field.click()
        search_field = self.switch_to_tab()
        return search_field
    

    def check_existance_block(self):
        '''Проверка наличие блока "Сила в людях"'''
        search_field = self.find_element(SbisLocators.LOCATOR_TENSOR_BLOCK_PEOPLE)
        return search_field.text


    def go_to_tensor_detail(self):
        '''Переход в блоке "Сила в людях" Подробнее на tensor/about'''
        search_field = self.find_element(SbisLocators.LOCATOR_TENSOR_DETAIL)
        self.driver.execute_script('arguments[0].click();', search_field)
        return search_field  
    

    def check_images(self):
        '''Проверят изображения в разделе "Работаем" на одинаковую высоту и ширину'''
        search_field = self.find_element(SbisLocators.LOCATOR_TENSOR_IMG_BY_TEXT)
        images = search_field.find_elements(By.TAG_NAME, 'img')
        result = {}
        for image in images:
            h = image.get_dom_attribute('height')
            w = image.get_dom_attribute('width')
            if not result:
                result['height'] = h
                result['weight'] = w
            elif (h and w) in result.values():
                continue
            else:
                result = {}
                break
        return True if len(result) == 2 else False
    

    def get_current_url(self):
        '''Возвращает текущий URL'''
        return self.driver.current_url
    
