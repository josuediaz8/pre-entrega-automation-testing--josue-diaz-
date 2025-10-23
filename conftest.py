import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_opt = Options() 
    chrome_opt.add_argument("--incognito") #abre chrome como incognito y desactiva ventana de contraseña
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()


@pytest.fixture
def login_in_diver (driver):
    login (driver)
    return driver