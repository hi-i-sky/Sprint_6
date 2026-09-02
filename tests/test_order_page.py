from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import pytest
import allure
from pages.order_page import OrderPage
from constants.main_page_constants import BASE_URL
from constants.order_page_constants import FIRST_TEST_DATA, SECOND_TEST_DATA, EXPECTED_SUCCESS_TEXT


class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        driver_path = GeckoDriverManager().install()
        firefox_service = Service(executable_path=driver_path)
        cls.driver = webdriver.Firefox(service=firefox_service)

    @allure.title('Проверяем флоу позитивного сценария заказа самоката')
    @pytest.mark.parametrize('test_data', [FIRST_TEST_DATA, SECOND_TEST_DATA])
    def test_order_scooter_success(self, test_data):
        self.driver.get(BASE_URL)

        order_page = OrderPage(self.driver)

        if test_data["entry_type"] == "top":
            order_page.click_top_order_button()
        elif test_data["entry_type"] == "bottom":
            order_page.click_bottom_order_button()

        order_page.wait_for_load_first_order_page()

        order_page.set_first_page_order(
        name=test_data["name"],
        surname=test_data["surname"],
        address=test_data["address"],
        station=test_data["station"],
        phone=test_data["phone"]
        )

        order_page.set_second_page_order(
        date_locator=test_data["date"],
        period_locator=test_data["period"],
        color_locator=test_data["color"],
        comment=test_data["comment"]
        )
        
        order_page.wait_for_load_confirm_window()
        order_page.confirm_order()
        order_page.wait_for_load_success_window()

        assert EXPECTED_SUCCESS_TEXT in order_page.get_success_text()

        order_page.close_success_order_creation_window()
        order_page.wait_for_load_status_of_order_page()

        if test_data["final_check"] == "home":
            order_page.click_home_button()
            order_page.wait_for_load_home_page()
        elif test_data["final_check"] == 'yandex':
            order_page.click_ya_button()
            order_page.wait_for_load_ya_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 