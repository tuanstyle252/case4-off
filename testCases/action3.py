from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from basetest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testaction3(BaseTest):

    def testaction3(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        time.sleep(2)
        #click cancel
        self.driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        check_click = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        try:
            assert check_click == True
            self.logger.info(f'Passed when validate the modal close')
        except Exception as ex:
            self.logger.error(f'Failed when validate the modal close '+ str(ex))

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        #click X
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@class='close']").click()
        check_click = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        try:
            assert check_click == True
            self.logger.info(f'Passed when validate the modal close')
        except Exception as ex:
            self.logger.error(f'Failed when validate the modal close ' + str(ex))

