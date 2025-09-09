import pytest
from selenium import webdriver
from config.config import TestConfig

@pytest.fixture
def setup_driver():
    driver = webdriver.Firefox()
    driver.get(TestConfig.BASE_URL)
    yield driver
    driver.quit()
