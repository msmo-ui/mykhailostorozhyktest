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
        job_list = self.qa.click_see_all_jobs().scroll_to_element_y_with_delay(700).click_drop_down_filter_by_location()\
            .click_drop_down_filter_by_location_element_istanbul_turkey()\
            .collected_list_of_text_elements_position_location()

        expected_text = "Istanbul, Turkey"

        for job in job_list:
            assert job.text == expected_text, "wrong text %s, expected %s" % (job.text, expected_text)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_check_redirect(self, setup):
        self.logger.info("************ Test_001_Quality_Assurance ************")
        self.logger.info("************ Verifying Quality Assurance Job List ************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL + "/careers/quality-assurance/")
        self.qa = QualityAssurance(self.driver)
        url=self.qa.click_see_all_jobs().scroll_to_element_y_with_delay(700).click_drop_down_filter_by_location()\
            .click_drop_down_filter_by_location_element_istanbul_turkey().click_view_role()

        assert "https://jobs.lever.co/" in url








