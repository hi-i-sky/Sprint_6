import sys
from pathlib import Path
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait


ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

@pytest.fixture(scope="class")
def driver():
    driver_path = GeckoDriverManager().install()
    firefox_service = Service(executable_path=driver_path)

    driver = webdriver.Firefox(service=firefox_service)
    yield driver
    driver.quit()