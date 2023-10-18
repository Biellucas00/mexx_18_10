import pytest
from paginas.loginpage import loginpage

@pytest.fixture()
def open_login():
    login_page = loginpage()
    yield login_page

