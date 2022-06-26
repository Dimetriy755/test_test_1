import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')  # - not need, because is used - autouse=True
class TestHomepage:

    def test_homepage(self):
        pass
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(10)
        # element_1 = driver.find_element(By.CSS_SELECTOR, "#id_123")
        #
        # wait = WebDriverWait(driver, 10, 0.3)
        # element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_321")))
