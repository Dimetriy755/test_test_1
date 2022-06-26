import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use '--headless' if you do not need a browser UI
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1366,768')
    # options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    service = Service(executable_path='C:\\chromedriver\\chromedriver.exe')
    options = get_chrome_options
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@pytest.fixture(scope='function', autouse=True)  # scope='function' - if you need a new clean browser tab
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    # driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

