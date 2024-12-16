from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cards = (By.CSS_SELECTOR, ".card.h-100")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardButton = (By.CSS_SELECTOR, ".card-footer button")
    checkoutBtn = (By.CSS_SELECTOR, "#navbarResponsive a")

    def cardsItem(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardButtons(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

    def getCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage