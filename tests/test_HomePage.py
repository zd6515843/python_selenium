import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])

        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckMeOut().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()
        alertText = homepage.getMessage().text
        assert ("Success" in alertText)

        time.sleep(3)

    # @pytest.fixture(params=[("Rahul", "shetty", "Male"),("Andy", "Zhang", "Female")])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param