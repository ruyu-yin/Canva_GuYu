
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='session')
def login():
    options = Options()
    options.add_experimental_option("detach",True)
    options.add_experimental_option('useAutomationExtension',False)
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('--remote-debugging-port=8201')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.canva.cn")
    driver.maximize_window()



