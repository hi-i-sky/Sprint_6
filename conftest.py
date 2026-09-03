import sys
from pathlib import Path
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from pages.order_page import OrderPage
from pages.main_page import MainPage


ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

@pytest.fixture(scope="class")
def driver():
    driver_path = GeckoDriverManager().install()
    firefox_service = Service(executable_path=driver_path)

    driver = webdriver.Firefox(service=firefox_service)
    yield driver
    driver.quit()

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.get_main_page()
    return page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_main_page()
    return page