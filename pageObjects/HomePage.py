from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.CSS_SELECTOR, "[name = 'name']")
    email = (By.NAME, "email")
    checkmeout = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "// input[ @ value = 'Submit']")
    message = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckMeOut(self):
        return self.driver.find_element(*HomePage.checkmeout)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
