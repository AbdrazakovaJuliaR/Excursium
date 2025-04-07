# Тесты фильтрации экскурсий

from locators import FilterPageLocators as loc
from settings import EXCURSIONS_URL

def test_filter_default_open(driver):
    driver.get(EXCURSIONS_URL)
    filters = driver.find_elements(*loc.FILTER_BLOCKS)
    assert all(f.is_displayed() for f in filters)

def test_show_more_button(driver):
    driver.get(EXCURSIONS_URL)
    buttons = driver.find_elements(*loc.SHOW_MORE_BUTTON)
    for btn in buttons:
        btn.click()
        assert len(driver.find_elements(By.CLASS_NAME, "option")) > 5