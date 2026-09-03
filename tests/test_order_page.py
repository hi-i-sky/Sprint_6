import allure
from pages.order_page import OrderPage
from constants.order_page_constants import TOP_NAME, TOP_SURNAME, TOP_ADDRESS, TOP_STATION, TOP_PHONE, TOP_COMMENT, BOTTOM_NAME, BOTTOM_SURNAME, BOTTOM_ADDRESS, BOTTOM_STATION, BOTTOM_PHONE, BOTTOM_COMMENT, EXPECTED_SUCCESS_TEXT
from locators.order_page_locators import DATE_10_BUTTON, THREE_DAYS_PERIOD_BUTTON, CHECKBOX_GREY, DATE_9_BUTTON, TWO_DAYS_PERIOD_BUTTON, CHECKBOX_BLACK


class TestOrderPage:


    @allure.title('Проверяем флоу позитивного сценария заказа самоката через кнопку наверху страницы')
    def test_order_scooter_by_top_order_button_success(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page()
        order_page.click_top_order_button()
        order_page.wait_for_load_first_order_page()

        order_page.set_first_page_order(TOP_NAME, TOP_SURNAME, TOP_ADDRESS, TOP_STATION, TOP_PHONE)
        order_page.set_second_page_order(DATE_9_BUTTON, TWO_DAYS_PERIOD_BUTTON, CHECKBOX_BLACK, TOP_COMMENT)
        
        order_page.wait_for_load_confirm_window()
        order_page.confirm_order()
        order_page.wait_for_load_success_window()

        assert EXPECTED_SUCCESS_TEXT in order_page.get_success_text()


    @allure.title('Проверяем флоу позитивного сценария заказа самоката через кнопку внизу страницы')
    def test_order_scooter_by_bottom_order_button_success(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page()
        order_page.click_bottom_order_button()
        order_page.wait_for_load_first_order_page()

        order_page.set_first_page_order(BOTTOM_NAME, BOTTOM_SURNAME, BOTTOM_ADDRESS, BOTTOM_STATION, BOTTOM_PHONE)
        order_page.set_second_page_order(DATE_10_BUTTON, THREE_DAYS_PERIOD_BUTTON, CHECKBOX_GREY, BOTTOM_COMMENT)
        
        order_page.wait_for_load_confirm_window()
        order_page.confirm_order()
        order_page.wait_for_load_success_window()

        assert EXPECTED_SUCCESS_TEXT in order_page.get_success_text()