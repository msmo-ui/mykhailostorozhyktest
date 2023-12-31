class HomePage:
    text_company_header_xpath = "//li/a[contains(text(),'Company')]"
    link_careers_page_linktext = "//div[contains(@class,'container')]/a[contains(@href,'careers')]"

    def __init__(self, driver):
        self.driver = driver

    def click_header_menu_element(self):
        self.driver.find_element("xpath", self.text_company_header_xpath).click()
        return self

    def click_sub_menu_header_element(self):
        self.driver.find_element("xpath", self.link_careers_page_linktext).click()
