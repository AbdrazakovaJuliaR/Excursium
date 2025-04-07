# Тест перехода по поиску на лендинге

from settings import BASE_URL
from locators import LandingPageLocators as loc

def test_redirect_from_empty_search(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.SEARCH_BUTTON).click()
    assert "/ekskursii-dlya-shkolnikov/list" in driver.current_url