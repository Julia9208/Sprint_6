import pytest
from selenium import webdriver
from config.urls import Urls

@pytest.fixture
def setup_driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
