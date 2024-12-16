import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)

        homePage.shopItems().click()

        log.info("getting all the card titles")
        cards = checkoutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if card.text == "Blackberry":
                checkoutPage.getCardButtons()[i].click()

        confirmpage = checkoutPage.getCheckoutButton()
        confirmpage.getCheckoutButton().click()
        log.info("Entering country name as Ind")
        confirmpage.getCountry().send_keys("Ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located(confirmpage.indiaOption)).click()

        self.verifyLinkPresence("India").click()
        confirmpage.getAgree().click()
        confirmpage.getPurchaseButton().click()
        textMatch = confirmpage.getMessage().text
        log.info("Text received from application is " + textMatch)
        assert "Success!" in textMatch
        time.sleep(3)



