# Все локаторы страниц

from selenium.webdriver.common.by import By

class RegisterPageLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    NAME = (By.NAME, "name")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

class LoginPageLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

class FilterPageLocators:
    FILTER_BLOCKS = (By.CLASS_NAME, "filter-block")
    SHOW_MORE_BUTTON = (By.XPATH, "//button[contains(text(),'Показать больше')]")
    RESULTS = (By.CLASS_NAME, "excursion-card")

class LandingPageLocators:
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search")

class BookingPageLocators:
    MIN_INPUT = (By.NAME, "min")
    MAX_INPUT = (By.NAME, "max")
    PRICE_BLOCK = (By.CLASS_NAME, "price")
    ALERT = (By.CLASS_NAME, "alert")