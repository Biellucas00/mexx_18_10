import time

from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class loginpage:
    url = "https://demo.2do.mexx.ai/pt"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(7)

        self.id_campo_email = (By.ID, 'email')
        self.id_campo_senha = (By.ID, 'password')
        self.id_entrar = (By.CLASS_NAME, 'MuiButton-root')

    def enter_username(self, username):
        self.driver.find_element(*self.id_campo_email).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.id_campo_senha).send_keys(password)

    def click_confirmar(self):
        self.driver.find_element(*self.id_entrar).click()
        script = """
            var buttons = document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++) {
              if (buttons[i].textContent === 'Confirmar') {
                buttons[i].click();
                break;
              }
            }
            """
        self.driver.execute_script(script)
        time.sleep(20)


