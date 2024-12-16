from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR, ".btn.btn-success")
    country = (By.CSS_SELECTOR, "#country")
    indiaOption = (By.XPATH, "//a[text()='India']")
    agree = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[type=submit]")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getCheckoutButton(self):
        return self.driver.find_element(*ConfirmPage.checkout)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getAgree(self):
        return self.driver.find_element(*ConfirmPage.agree)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getMessage(self):
        return self.driver.find_element(*ConfirmPage.message)