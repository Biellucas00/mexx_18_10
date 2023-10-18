import time
import pytest
from selenium import webdriver
from paginas.loginpage import loginpage

class Test_principal():

    def setup_method(self):
        # Inicialize o driver aqui
        self.driver = webdriver.Firefox()

    def teardown_method(self):
        # Encerre o driver aqui
        self.driver.quit()

    def test_01(self):
        self.email_login = "lucasgabrielinhalt@gmail.com"
        self.senha_login = "123456"

        ##instancia com a pagina de login
        login_page = loginpage(self.driver)

        ##metodos da pagina

        login_page.enter_username(self.email_login)
        login_page.enter_password(self.senha_login)
        login_page.click_confirmar()

