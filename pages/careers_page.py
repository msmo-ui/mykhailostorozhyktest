from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class CareersPage:
    button_teams_load_more = "//div[@class = 'row']/a"
    link_quality_assurance = "//a[contains(@href,'quality-assurance')]/h3"
    text_life_at_insider = "//h2[contains(text(),'Life at Insider')]"

    def __init__(self, driver):
        self.driver = driver

    def click_load_more(self):
        self.driver.find_element("xpath", self.button_teams_load_more).click()

    def scroll_to_element_y(self, delta_y):
        scroll_origin = ScrollOrigin.from_viewport(10, 10)
        ActionChains(self.driver) \
            .scroll_from_origin(scroll_origin, 0, delta_y) \
            .perform()
        sleep(0.5)
        return self

    def find_load_more_button(self):
        load_more = self.driver.find_element("xpath", self.button_teams_load_more)
        return load_more

    def find_life_at_insider(self):
        load_more = self.driver.find_element("xpath", self.text_life_at_insider)
        return load_more
