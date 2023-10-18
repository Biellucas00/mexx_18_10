import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_criarchamados:

    def __init__(self, driver):
        self.driver = driver

    def botao_criar_chamado(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/main/main/div/div[1]/div[1]/a').click()
        time.sleep(10)
