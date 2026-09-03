import pytest
import allure
from pages.order_page import OrderPage
from constants.order_page_constants import FIRST_TEST_DATA, SECOND_TEST_DATA, EXPECTED_SUCCESS_TEXT


class TestOrderPage:

    @allure.title('Проверяем флоу позитивного сценария заказа самоката')
    @pytest.mark.parametrize('test_data', [FIRST_TEST_DATA, SECOND_TEST_DATA])
    def test_order_scooter_success(self, driver, test_data):

        order_page = OrderPage(driver)
        order_page.get_main_page()

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


    @allure.title('Проверяем кнопку с логотипом Яндекса на главной странице')
    def test_ya_button(self, driver):

        order_page = OrderPage(driver)
        order_page.get_main_page()
        order_page.click_ya_button()
        order_page.wait_for_load_ya_page()


    @allure.title('Проверяем кнопку с логотипом Самоката на главной странице')
    def test_home_button(self, driver):

        order_page = OrderPage(driver)
        order_page.get_main_page()
        order_page.click_home_button()
        order_page.wait_for_load_home_page()