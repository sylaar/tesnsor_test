from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    '''Инициализирует драйвер и принимает стартовый URL'''

    def __init__(self, base_url: str):
        self.driver = webdriver.Chrome()
        self.base_url = base_url


    def find_element(self, locator, time=2):
        '''Поиск элемента по заданному локатору'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Cant find element by locator {locator}')
    
    
    def find_elements(self, locator, time=2):
        '''Поиск элементов по заданному локатору'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Cant find elements by locator {locator}')
    

    def switch_to_tab(self):
        '''Переключение драйвера на нрвую вкладку'''
        return self.driver.switch_to.window(self.driver.window_handles[1])


    def go_to_site(self):
        '''Переход на стартовый URL'''
        return self.driver.get(self.base_url)