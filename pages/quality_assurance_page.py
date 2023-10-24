from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class QualityAssurance:
    button_see_all_jobs = "//div[contains(@class, 'row')]/a"
    drop_down_filter_by_location = "//span[@title = 'All']"
    drop_down_filter_by_location_element_istanbul_turkey = "//li[contains(@id, 'Istanbul, Turkey')]"
    drop_down_filter_by_department = "//span[@title = 'Quality Assurance']"
    wrapper_element_for_job_opportunities = "//div[@class = 'position-list-item-wrapper bg-light']"
    text_inside_wrapper_position_location = "//div[@class = 'position-list-item-wrapper bg-light']/div"
    text_inside_wrapper_position_department = "//div[@class = 'position-list-item-wrapper bg-light']/span"
    iframe_inside_wrapper_position_department = "//div[@class = 'position-list-item-wrapper bg-light']/span"

    button_only_necessary_cookies = "//div[contains(@class,  'row')]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_see_all_jobs(self):
        self.driver.find_element("xpath", self.button_see_all_jobs).click()

    def click_drop_down_filter_by_location(self):
        self.driver.find_element("xpath", self.drop_down_filter_by_location).click()

    def click_drop_down_filter_by_location_element_istanbul_turkey(self):
        self.driver.find_element("xpath", self.drop_down_filter_by_location_element_istanbul_turkey).click()
        sleep(1.5)

    def scroll_to_element_y_with_delay(self, delta_y):
        scroll_origin = ScrollOrigin.from_viewport(10, 10)
        ActionChains(self.driver) \
            .scroll_from_origin(scroll_origin, 0, 700) \
            .perform()
        sleep(3.5)

    def collected_list_of_text_elements_position_location(self):
        position_locations_elements = self.driver.find_elements("xpath", self.text_inside_wrapper_position_location)
        return position_locations_elements
