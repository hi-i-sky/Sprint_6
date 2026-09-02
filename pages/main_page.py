from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(self.driver, 5)

    def get_answer_for_question(self, question_locator, answer_locator):
        question = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

        answer = self.driver.find_element(*answer_locator)
        self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text
