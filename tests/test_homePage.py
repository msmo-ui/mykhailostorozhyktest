import pytest

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestHome:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("************ Test_001_Home ************")
        self.logger.info("************ Verifying Home Page Title ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "#1 Leader in Individualized, Cross-Channel CX — Insider":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title test is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home Page Title test is failed ************")
            assert False

    @pytest.mark.sanity
    def test_click_header_menu_company_careers(self, setup):
        self.logger.info("************ Test_002_Home ************")
        self.logger.info("************ Verifying Careers Page Title ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.click_header_menu_element().click_sub_menu_header_element()
        self.cp = CareersPage(self.driver)
        act_title = self.driver.title

        if act_title == "Insider Careers":
            assert True
            self.driver.close()
            self.logger.info("************ Careers Page Title test is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_careersPageTitle.png")
            self.driver.close()
            self.logger.error("************ Careers Page Title test is failed ************")
            assert False
