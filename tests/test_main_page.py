import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import QUESTION_PRICE, ANSWER_PRICE, QUESTION_SEVERAL_SCOOTERS, ANSWER_SEVERAL_SCOOTERS, QUESTION_RENTAL_TIME, ANSWER_RENTAL_TIME, QUESTION_ORDER_FOR_TODAY, ANSWER_ORDER_FOR_TODAY, QUESTION_EXTEND_ORDER, ANSWER_EXTEND_ORDER, QUESTION_CHARGER, ANSWER_CHARGER, QUESTION_ORDER_CANCELLATION, ANSWER_ORDER_CANCELLATION, QUESTION_ORDER_OUTSIDE_MOSCOW, ANSWER_ORDER_OUTSIDE_MOSCOW
from constants.main_page_constants import TEXT_PRICE, TEXT_SEVERAL_SCOOTERS, TEXT_RENTAL_TIME, TEXT_ORDER_FOR_TODAY, TEXT_EXTEND_ORDER, TEXT_CHARGER, TEXT_ORDER_CANCELLATION, TEXT_ORDER_OUTSIDE_MOSCOW


class TestMainPage:


    @allure.title('Проверяем тексты ответов на вопросы в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        [QUESTION_PRICE, ANSWER_PRICE, TEXT_PRICE],
        [QUESTION_SEVERAL_SCOOTERS, ANSWER_SEVERAL_SCOOTERS, TEXT_SEVERAL_SCOOTERS],
        [QUESTION_RENTAL_TIME, ANSWER_RENTAL_TIME, TEXT_RENTAL_TIME],
        [QUESTION_ORDER_FOR_TODAY, ANSWER_ORDER_FOR_TODAY, TEXT_ORDER_FOR_TODAY],
        [QUESTION_EXTEND_ORDER, ANSWER_EXTEND_ORDER, TEXT_EXTEND_ORDER],
        [QUESTION_CHARGER, ANSWER_CHARGER, TEXT_CHARGER],
        [QUESTION_ORDER_CANCELLATION, ANSWER_ORDER_CANCELLATION, TEXT_ORDER_CANCELLATION],
        [QUESTION_ORDER_OUTSIDE_MOSCOW, ANSWER_ORDER_OUTSIDE_MOSCOW, TEXT_ORDER_OUTSIDE_MOSCOW]
    ])
    def test_check_answer_for_question(self, driver, question_locator, answer_locator, expected_text):

        main_page = MainPage(driver)
        main_page.get_main_page()
        result_text = main_page.get_answer_for_question(question_locator, answer_locator)

        assert expected_text == result_text