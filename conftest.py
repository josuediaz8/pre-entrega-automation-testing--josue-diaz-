import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver #yield se usa con fixture, permite ejecutaqr la prueba en el medio / se pausa el codigo
    driver.quit()

@pytest.fixture
def login_in_diver (driver):
    login (driver)
    return driver