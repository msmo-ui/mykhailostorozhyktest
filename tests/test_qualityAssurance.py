import pytest

from pages.quality_assurance_page import QualityAssurance
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestQualityAssurance:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_check_list_of_qa_positions(self, setup):
        self.logger.info("************ Test_001_Quality_Assurance ************")
        self.logger.info("************ Verifying Quality Assurance Job List ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL + "/careers/quality-assurance/")
        self.qa = QualityAssurance(self.driver)
        self.qa.click_see_all_jobs()
        self.qa.scroll_to_element_y_with_delay(700)
        self.qa.click_drop_down_filter_by_location()
        self.qa.click_drop_down_filter_by_location_element_istanbul_turkey()
        job_list = self.qa.collected_list_of_text_elements_position_location()

        try:
            assert job_list is not None
            self.driver.close()
            self.logger.info("************ Quality Assurance Job List has elements ************")  # 👉️ Oulu
        except KeyError:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_qualityAssurance.png")
            self.driver.close()
            self.logger.error("************ Quality Assurance Job List has no elements ************")
