from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class QualityAssurance:
    button_see_all_jobs = "//div[contains(@class, 'row')]/a"
    drop_down_filter_by_location = "//span[@title = 'All']"
    drop_down_filter_by_location_element_istanbul_turkey = "//li[contains(@id, 'Istanbul, Turkey')]"
    drop_down_filter_by_department = "//span[@title = 'Quality Assurance']"
    wrapper_element_for_job_opportunities = "//div[@class = 'position-list-item-wrapper bg-light']"
    text_inside_wrapper_position_location = "//div[@class = 'position-list-item-wrapper bg-light']/div"
    text_inside_wrapper_position_department = "//div[@class = 'position-list-item-wrapper bg-light']/span"
    iframe_inside_wrapper_position_department = "//div[@class = 'position-list-item-wrapper bg-light']/span"

    view_role_element_1 = "//html/body/section[3]/div/div/div[2]/div[1]/div/a"
    first_element = "//html/body/section[3]/div/div/div[2]/div[1]/div"

    button_only_necessary_cookies = "//div[contains(@class,  'row')]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_see_all_jobs(self):
        self.driver.find_element("xpath", self.button_see_all_jobs).click()
        return self

    def click_drop_down_filter_by_location(self):
        self.driver.find_element("xpath", self.drop_down_filter_by_location).click()
        return self

    def click_drop_down_filter_by_location_element_istanbul_turkey(self):
        sleep(2)
        self.driver.find_element("xpath", self.drop_down_filter_by_location_element_istanbul_turkey).click()
        sleep(2)
        return self

    def scroll_to_element_y_with_delay(self, delta_y):
        scroll_origin = ScrollOrigin.from_viewport(10, 10)
        ActionChains(self.driver) \
            .scroll_from_origin(scroll_origin, 0, 700) \
            .perform()
        sleep(3.5)
        return self

    def collected_list_of_text_elements_position_location(self) -> list[WebElement]:
        position_locations_elements = self.driver.find_elements("xpath", self.text_inside_wrapper_position_location)
        return position_locations_elements

    def click_view_role(self):
        sleep(3)
        self.driver.find_element("xpath", self.view_role_element_1)
        self.driver.find_element("xpath", self.view_role_element_1).click()
        sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[1])

        return self.driver.current_url
