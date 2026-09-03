from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from locators.order_page_locators import TOP_ORDER_BUTTON, BOTTOM_ORDER_BUTTON, NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, STATION_FIELD, STATION_DROPDOWN_LIST, PHONE_FIELD, CONFIRM_BUTTON, BACK_BUTTON, DATE_FIELD, DATEPICKER, PERIOD_FIELD, PERIOD_MENU, COMMENT_FIELD, SAVE_BUTTON, SUCCESS_WINDOW, VIEW_STATUS_BUTTON, YA_BUTTON, HOME_BUTTON, CONTINUE_BUTTON
from constants.main_page_constants import YA_URL, BASE_URL


class OrderPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_top_order_button(self):
        self.driver.find_element(*TOP_ORDER_BUTTON).click()

    def click_bottom_order_button(self):
        bottom_button = self.driver.find_element(*BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bottom_button)
        bottom_button.click()

    def wait_for_load_first_order_page(self):
        self.wait.until(EC.visibility_of_element_located(CONTINUE_BUTTON))

    def set_name(self, name):
        self.driver.find_element(*NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)

    def set_station(self, station):
        self.driver.find_element(*STATION_FIELD).send_keys(station)
        self.wait.until(EC.visibility_of_element_located(STATION_DROPDOWN_LIST))

        xpath_for_station = f".//div[text()='{station}']"

        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_for_station))) 
        self.driver.find_element(By.XPATH, xpath_for_station).click()

    def set_phone(self, phone):
        self.driver.find_element(*PHONE_FIELD).send_keys(phone)

    def click_continue_button(self):
        self.driver.find_element(*CONTINUE_BUTTON).click()

    def set_first_page_order(self, name, surname, address, station, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)
        self.click_continue_button()

    def wait_for_load_second_order_page(self):
        self.wait.until(EC.visibility_of_element_located(BACK_BUTTON))

    def set_date(self, date_locator):
        self.driver.find_element(*DATE_FIELD).click()
        self.wait.until(EC.visibility_of_element_located(DATEPICKER))
        self.driver.find_element(*date_locator).click()

    def set_period(self, period_locator):
        self.driver.find_element(*PERIOD_FIELD).click()
        self.wait.until(EC.visibility_of_element_located(PERIOD_MENU))
        self.driver.find_element(*period_locator).click()

    def set_color(self, color_locator):
        self.driver.find_element(*color_locator).click()

    def set_comment(self, comment):
        self.driver.find_element(*COMMENT_FIELD).send_keys(comment)

    def click_save_button(self):
        self.driver.find_element(*SAVE_BUTTON).click()

    def set_second_page_order(self, date_locator, period_locator, color_locator, comment):
        self.set_date(date_locator)
        self.set_period(period_locator)
        self.set_color(color_locator)
        self.set_comment(comment)
        self.click_save_button()

    def wait_for_load_confirm_window(self):
        self.wait.until(EC.element_to_be_clickable(CONFIRM_BUTTON))

    def confirm_order(self):
        self.driver.find_element(*CONFIRM_BUTTON).click()

    def wait_for_load_success_window(self):
        self.wait.until(EC.element_to_be_clickable(VIEW_STATUS_BUTTON))

    def get_success_text(self):
        return self.driver.find_element(*SUCCESS_WINDOW).text

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