from selenium.webdriver.common.by import By
import time
import consts
from pageObjects.BasePage import BasePage

_email_locator = "//*[@id='identifierId']"
_gmail = "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]/div[2]"
_password_locator = "//*[@id='password']/div[1]/div/div[1]/input"
_next_username_btn_locator = "//*[@id='identifierNext']/div/button/span"
_next_password_btn_locator = "//*[@id='passwordNext']/div/button"


class Loginpage(BasePage):

    def login(self, credentials):

        self.driver.find_element(By.XPATH, _gmail).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, _email_locator).send_keys(credentials.email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, _next_username_btn_locator).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, _password_locator).send_keys(credentials.password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, _next_password_btn_locator).click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='instant-search']").send_keys("Yak hotel natal")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='hotel-select-container']/div[3]/table/tbody/tr/td[2]/a").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='rev-navbar-menu']/nav/div[1]/div[5]").click()
        time.sleep(1)

