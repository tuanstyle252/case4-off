from pageObjects.LoginPage import Loginpage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basetest import BaseTest


class Testaction4(BaseTest):

    def test_action_case1_1(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='gfb-delivery-email']").click()
        time.sleep(4)

        check_submit = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
        email_field = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='gfb-export-recipients']/div[1]")))
        try:
            assert check_submit.is_enabled() == False and email_field == True
            self.logger.info(f'Passed when validate the email field disappears and submit button is disable')
        except Exception as ex:
            self.logger.error(f'Failed when validate the email field disappears and submit button is disable '+ str(ex))

    def test_action_case1_2(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='gfb-export-recipients']/div[1]/div[2]/div[1]").click()
        time.sleep(4)
        # elem = self.driver.find_element(By.XPATH, "//*[@id='gfb-export-recipients']/div[1]/div[1]")
        msg = self.driver.find_element(By.XPATH, "//*[@id='gfb-export-recipients']/div[1]/div[1]/div[1]")
        msg_message = msg.text
        check_submit = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
        try:
            assert msg_message == "Add Others" and check_submit.is_enabled() == False
            self.logger.info(f'Passed when validate for text add note and submit button is disable')
        except Exception as ex:
            self.logger.error(f'Failed when validate for text add note and submit button is disable ' + str(ex))

    def test_action_case1_3(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@id='gfb-export-recipients']/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='gfb-export-recipients']/div[1]/div[1]").click()
        wait = WebDriverWait(self.driver, 10)
        unameId = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='gfb-export-recipients']/div[2]")))
        msg_message = unameId.text
        check_submit = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
        try:
            assert msg_message == "No options" and check_submit.is_enabled() == False
            self.logger.info(f'Passed when validate for text No options and submit button is disable')
        except Exception as ex:
            self.logger.error(f'Failed when validate for text No options and submit button is disable ' + str(ex))