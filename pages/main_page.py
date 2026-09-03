from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants.main_page_constants import YA_URL, BASE_URL
from locators.order_page_locators import TOP_ORDER_BUTTON, BOTTOM_ORDER_BUTTON, YA_BUTTON, HOME_BUTTON


class MainPage:


    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(self.driver, 5)

    def get_main_page(self):
        self.driver.get(BASE_URL)

    def click_top_order_button(self):
        self.driver.find_element(*TOP_ORDER_BUTTON).click()

    def click_bottom_order_button(self):
        bottom_button = self.driver.find_element(*BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bottom_button)
        bottom_button.click()

    def get_answer_for_question(self, question_locator, answer_locator):
        question = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

        answer = self.driver.find_element(*answer_locator)
        self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text

    def click_ya_button(self):
        self.driver.find_element(*YA_BUTTON).click()
        
        self.wait.until(lambda d: len(d.window_handles) > 1)
        
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def click_home_button(self):
        self.driver.find_element(*HOME_BUTTON).click()

    def wait_for_load_ya_page(self):
        self.wait.until(EC.url_contains(YA_URL))

    def wait_for_load_home_page(self):
        self.wait.until(EC.url_to_be(BASE_URL))