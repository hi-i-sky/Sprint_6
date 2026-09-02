from selenium.webdriver.common.by import By

QUESTION_PRICE = [By.ID, 'accordion__heading-0']
QUESTION_SEVERAL_SCOOTERS = [By.ID, 'accordion__heading-1']
QUESTION_RENTAL_TIME = [By.ID, 'accordion__heading-2']
QUESTION_ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']
QUESTION_EXTEND_ORDER = [By.ID, 'accordion__heading-4']
QUESTION_CHARGER = [By.ID, 'accordion__heading-5']
QUESTION_ORDER_CANCELLATION = [By.ID, 'accordion__heading-6']
QUESTION_ORDER_OUTSIDE_MOSCOW = [By.ID, 'accordion__heading-7']

ANSWER_PRICE = [By.XPATH, './/div[@aria-labelledby="accordion__heading-0"]/p']
ANSWER_SEVERAL_SCOOTERS = [By.XPATH, './/div[@aria-labelledby="accordion__heading-1"]/p']
ANSWER_RENTAL_TIME = [By.XPATH, './/div[@aria-labelledby="accordion__heading-2"]/p']
ANSWER_ORDER_FOR_TODAY = [By.XPATH, './/div[@aria-labelledby="accordion__heading-3"]/p']
ANSWER_EXTEND_ORDER = [By.XPATH, './/div[@aria-labelledby="accordion__heading-4"]/p']
ANSWER_CHARGER = [By.XPATH, './/div[@aria-labelledby="accordion__heading-5"]/p']
ANSWER_ORDER_CANCELLATION = [By.XPATH, './/div[@aria-labelledby="accordion__heading-6"]/p']
ANSWER_ORDER_OUTSIDE_MOSCOW = [By.XPATH, './/div[@aria-labelledby="accordion__heading-7"]/p']
