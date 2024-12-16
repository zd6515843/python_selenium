import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self, element, text):
        sel = Select(element)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)

        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happened")
        # logger.critical("Critical issue")

        return logger