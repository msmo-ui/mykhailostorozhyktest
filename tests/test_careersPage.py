import pytest

from pages.careers_page import CareersPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestCareer:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_check_teams_button_element(self, setup):
        self.logger.info("************ Test_001_Career ************")
        self.logger.info("************ Verifying Careers Page Teams Element ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL + "/careers/")
        self.cp = CareersPage(self.driver)
        load_more = self.cp.scroll_to_element_y(2800).find_load_more_button().text

        if load_more.__contains__("teams"):
            assert True
            self.driver.close()
            self.logger.info("************ Careers Page See all teams has teams in the text ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_careersSeeAllTeams.png")
            self.driver.close()
            self.logger.error("************ Careers Page See all teams has no teams in the text ************")
            assert False

    @pytest.mark.sanity
    def test_check_life_insider_element(self, setup):
        self.logger.info("************ Test_002_Career ************")
        self.logger.info("************ Verifying Careers Page Life at Insider Element ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL + "/careers/")
        self.cp = CareersPage(self.driver)
        life_insider = self.cp.scroll_to_element_y(3800).find_life_at_insider().text

        if life_insider == "Life at Insider":
            assert True
            self.driver.close()
            self.logger.info("************ Careers Page life_insider == Life at Insider text ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_careersLifeInsider.png")
            self.driver.close()
            self.logger.error("************ Careers Page life_insider != Life at Insider text ************")
            assert False
