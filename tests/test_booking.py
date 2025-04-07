# Тесты калькулятора/бронирования
from settings import EXCURSIONS_URL
from locators import BookingPageLocators as loc

def test_invalid_booking_range(driver):
    driver.get(EXCURSIONS_URL)
    driver.find_element(*loc.MIN_INPUT).clear()
    driver.find_element(*loc.MIN_INPUT).send_keys("-1")
    driver.find_element(*loc.MAX_INPUT).clear()
    driver.find_element(*loc.MAX_INPUT).send_keys("1000")
    assert driver.find_element(*loc.ALERT).is_displayed()

def test_discount_calculation(driver):
    driver.get(EXCURSIONS_URL)
    driver.find_element(*loc.MIN_INPUT).clear()
    driver.find_element(*loc.MIN_INPUT).send_keys("10")
    driver.find_element(*loc.MAX_INPUT).clear()
    driver.find_element(*loc.MAX_INPUT).send_keys("15")
    price = driver.find_element(*loc.PRICE_BLOCK).text
    assert "₽" in price