from BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class SbisLocators:
    '''Задает локатары для конкретного сценария'''
    LOCATOR_SBIS_CONTACTS_PAGE = (By.CSS_SELECTOR, 'li.sbisru-Header__menu-item:nth-child(2) > a:nth-child(1)')
    LOCATOR_SBIS_CONTACTS_REGION = (By.CSS_SELECTOR, '.ml-16 > span:nth-child(1)')
    LOCATOR_SBIS_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__col')
    LOCATOR_SBIS_CHOOSE_REGION = (By.CSS_SELECTOR, '.ml-16 > span:nth-child(1)')
    LOCATOR_SBIS_NEW_REGION = (By.XPATH, '//span[text()="41 Камчатский край"]')


class SbisScript2(BasePage):
    '''Класс сценария тестирования'''

    def go_to_sbis_contacts(self):
        '''Переход на https://sbis/contacts'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_CONTACTS_PAGE)
        search_field.click()
        return search_field
    
    
    def check_region(self, locator):
        '''Возвращает текущий регион'''
        search_field = self.find_element(locator)
        return search_field.text

    
    def search_partners_list(self, locator):
        '''Возвращает текст списка партнеров'''
        search_field = self.find_element(locator)
        return search_field.text


    def choose_region(self):
        '''Изменяет регион на Камчатский край'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_CHOOSE_REGION)
        search_field.click()
        time.sleep(1)
        new_region = self.find_element(SbisLocators.LOCATOR_SBIS_NEW_REGION)
        new_region.click()
        time.sleep(1)
        return search_field
    

    def check_new_region(self):
        '''Возвращает True, если в URL присутствует "kamchatskij-kraj" и в title страницы есть подстрока "Камчатский край"'''
        url = self.get_current_url().find('kamchatskij-kraj')
        title = self.driver.title.find('Камчатский край')
        return (url, title)


    def get_current_url(self):
        '''Возвращает текущий URL'''
        return self.driver.current_url