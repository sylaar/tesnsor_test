from BasePage import BasePage
from selenium.webdriver.common.by import By
import requests, time, os



class SbisLocators:
    '''Задает локатары для конкретного сценария'''
    LOCATOR_SBIS_DOWNLOAD = (By.LINK_TEXT, 'Скачать СБИС')
    LOCATOR_SBIS_PLUGIN = (By.CLASS_NAME, 'sbis_ru-VerticalTabs__left')
    LOCATOR_SBIS_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__col')
    LOCATOR_SBIS_DOWNLOAD_WEB_INSTALLER = (By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

class SbisScript3(BasePage):
    '''Класс сценария тестирования'''

    def go_to_download_sbis(self):
        '''Переходит на "Скачать СБИС и дополнительное ПО"'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_DOWNLOAD)
        self.driver.execute_script('arguments[0].click();', search_field)
        time.sleep(1)
        return search_field
    

    def go_to_sbis_plugin(self):
        '''Переходит на "СБИС Палгин"'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_PLUGIN)
        result = search_field.find_elements(By.CLASS_NAME, 'controls-TabButton__caption')
        self.driver.execute_script('arguments[0].click();', result[1])
        time.sleep(1)


    def download_web_installer(self):
        '''Скачивает Веб-установщик и возвращает размер файла в Мб'''
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_DOWNLOAD_WEB_INSTALLER)
        url = search_field.get_dom_attribute('href')        
        try:
            r = requests.get(url)
        except Exception as e:
            print(e)
        else:
            file_extension = '.exe'
            # Если в конце url нет расширения, добавить его
            if file_extension not in url.split('/')[-1]:
                file_name = f'{url.split("/")[-1]}{file_extension}'
            # Иначе - взять последнюю часть url как file_name
            else:
                file_name = url.split('/')[-1]
            with open(file_name, 'wb') as file:
                file.write(r.content)
            os.rename(file_name, os.getcwd() + '/' + file_name)
            file_size = os.path.getsize(os.getcwd() + '/' + file_name)
        finally:
            return  round(file_size/1000000, 2) if file_size else None