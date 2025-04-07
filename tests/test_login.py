# Тесты авторизации

from test_data import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD
from settings import BASE_URL
from locators import LoginPageLocators as loc

def test_successful_login(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(*loc.EMAIL).send_keys(VALID_EMAIL)
    driver.find_element(*loc.PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*loc.SUBMIT).click()
    assert BASE_URL in driver.current_url or "dashboard" in driver.current_url

def test_failed_login(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(*loc.EMAIL).send_keys(INVALID_EMAIL)
    driver.find_element(*loc.PASSWORD).send_keys(INVALID_PASSWORD)
    driver.find_element(*loc.SUBMIT).click()
    assert driver.find_element(*loc.ERROR_MESSAGE).is_displayed()