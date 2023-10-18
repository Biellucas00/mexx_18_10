import time
import pytest
from selenium import webdriver
from paginas.loginpage import loginpage
from teste01 import Test_principal
from paginas.criar_chamado import Test_criarchamados


class Test_chamados(Test_principal):

    def test_02(self):
        # Passa o driver da classe pai (Test_principal) para a classe Test_criarchamados
        chamados = Test_criarchamados(self.driver)
        chamados.botao_criar_chamado()
