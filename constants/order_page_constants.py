from locators.order_page_locators import (
    DATE_9_BUTTON,
    DATE_10_BUTTON,
    TWO_DAYS_PERIOD_BUTTON,
    THREE_DAYS_PERIOD_BUTTON,
    CHECKBOX_BLACK,
    CHECKBOX_GREY,
)

FIRST_TEST_DATA = {
    "entry_type": "top",
    "name": "Анастасия",
    "surname": "Сафронова",
    "address": "Госпитальный переулок, д. 4, стр. 1",
    "station": "Бауманская",
    "phone": "+79990000000",
    "comment": "Проходная в общежитии, позвоните, как подойдете",
    "date": DATE_9_BUTTON,
    "period": TWO_DAYS_PERIOD_BUTTON,
    "color": CHECKBOX_BLACK
}

SECOND_TEST_DATA ={
    "entry_type": "bottom",
    "name": "Александр",
    "surname": "Абраменко",
    "address": "пр. Ленина, 1",
    "station": "Сокольники",
    "phone": "+79991111111",
    "comment": "Не опаздывайте, пожалуйста",
    "date": DATE_10_BUTTON,
    "period": THREE_DAYS_PERIOD_BUTTON,
    "color": CHECKBOX_GREY
}

EXPECTED_SUCCESS_TEXT = 'Заказ оформлен'