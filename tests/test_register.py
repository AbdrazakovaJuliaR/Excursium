# Тесты регистрации

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import RegisterPageLocators as loc
from settings import BASE_URL
from test_data import *
from faker import Faker

fake = Faker()

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*loc.EMAIL).send_keys(fake.email())
    driver.find_element(*loc.PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*loc.NAME).send_keys(NAME)
    driver.find_element(*loc.SUBMIT).click()
    assert BASE_URL in driver.current_url or "dashboard" in driver.current_url