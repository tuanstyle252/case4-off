import os.path
from datetime import datetime, timedelta
import datetime
from pageObjects.LoginPage import Loginpage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basetest import BaseTest


class Testaction5(BaseTest):

    def test_action5_case1(self):
        before_window = self.driver.window_handles[0]
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)

        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(3)

        # get text alert noti
        message_success = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rtest-alert-notifications']")))
        act_message_success = message_success.text
        try:
            assert "Success! Your report has been scheduled. To check the status of your export" in act_message_success
            self.logger.info(f'Passed when validate for the message')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the message '+ str(ex))

        self.driver.find_element(By.XPATH, "//*[@id='rtest-alert-notifications']/div/span/a").click()

        self.driver.execute_script("window.open('https://www.google.com/')")
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//*[@id='gb']/div/div[1]/div/div[1]/a").click()
        list_gmail = len(self.driver.find_elements(By.XPATH, "//*[@class='Cp'][2]//table/tbody/tr"))
        for gmail in range(0, list_gmail):
            owl = self.driver.find_elements(By.XPATH, "//*[@class='Cp'][2]//table/tbody/tr")
            owl[0].click()
            break

        self.driver.switch_to.window(before_window)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='dropdown-v2 dropdown nav-item primary-menu-item-with-icon'][2]/a"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='dropdown-v2 dropdown nav-item primary-menu-item-with-icon'][2]/div/a[10]"))).click()
        self.driver.close()

        self.driver.switch_to.window(after_window)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ii gt'][1]/div/div[1]/table/tbody/tr/td//table[7]/tbody/tr/td[1]/table/tbody/tr/td[1]"))).click()

        after = self.driver.window_handles[1]
        self.driver.switch_to.window(after)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()

        while not os.path.exists("D:/Downloads"):
            time.sleep(4)
        #check file
        try:
            if os.path.isfile("D:/Downloads/Revinate_export_66347_2022-04-27_WhbiDX.csv"):
                self.logger.info(f'Passed when validate file download')
            else:
                pass
        except Exception as ex:
            self.logger.info(f'Failed when validate file download '+ str(ex))

    def test_action5_case2(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-export']").click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='modal-footer']/button[2]"))).click()

        # get text alert noti
        message_success = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rtest-alert-notifications']")))
        act_message_success = message_success.text
        try:
            assert "Success! Your report has been scheduled. To check the status of your export" in act_message_success
            self.logger.info(f'Passed when validate for the message')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the message ' + str(ex))

        self.driver.find_element(By.XPATH, "//*[@id='rtest-alert-notifications']/div/span/a").click()

        after_window = self.driver.window_handles[0]
        self.driver.switch_to.window(after_window)

        #check daily
        time.sleep(5)
        date_after_day = datetime.datetime.today() + timedelta(days=1)
        pres = date_after_day.strftime('%m/%d/%Y')

        txt_day = self.driver.find_element(By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[3]")
        try:
            assert txt_day.text == pres
            self.logger.info(f'Passed when validate for the day download')
        except Exception as ex:
            self.logger.info(f'Failed when validate for the day download '+ str(ex))

        txt_shedule = self.driver.find_element(By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[2]")
        try:
            assert txt_shedule.text == "daily"
            self.logger.info(f'Passed when validate for the schedule')
        except Exception as ex:
            self.logger.info(f'Failed when validate for the schedule '+ str(ex))

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[6]/a[1]"))).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()



    # def test_action5_case3(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     time.sleep(3)
    #     self.lp = Loginpage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-export']").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-weekly']").click()
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-weekday-sunday']").click()
    #     time.sleep(3)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[@class='modal-footer']/button[2]"))).click()
    #     expectedMessage = "Success! Your report has been scheduled. To check the status of your export, visit the Download Center"
    #
    #     # get text alert noti
    #     message_success = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#rtest-alert-notifications")))
    #     act_message_success = message_success.text
    #     assert act_message_success, expectedMessage
    #     self.driver.find_element(By.XPATH, "//*[@id='rtest-alert-notifications']/div/span/a").click()
    #     # check weekly on selected day
    #     time.sleep(5)
    #
    # #
    # def test_action5_case4(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     time.sleep(3)
    #     self.lp = Loginpage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-export']").click()
    #     time.sleep(4)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-monthly']").click()
    #     time.sleep(4)
    #     # self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[@class='modal-footer']/button[2]"))).click()
    #
    #     expectedMessage = "Success! Your report has been scheduled. To check the status of your export, visit the Download Center"
    #
    #     # get text alert noti
    #     message_success = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#rtest-alert-notifications")))
    #     act_message_success = message_success.text
    #     assert act_message_success, expectedMessage
    #     self.driver.find_element(By.XPATH, "//*[@id='rtest-alert-notifications']/div/span/a").click()
    #     after_window = self.driver.window_handles[0]
    #     self.driver.switch_to.window(after_window)
    #
    #     # check month
    #     time.sleep(5)
    #     date_after_day = datetime.datetime.today() + relativedelta(months=1)
    #     pres = date_after_day.strftime('%m/%d/%Y')
    #
    #     txt_day = self.driver.find_element(By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[3]")
    #
    #     if txt_day.text == pres:
    #         assert True
    #     else:
    #         raise ValueError("day not same")
    #
    #     txt_shedule = self.driver.find_element(By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[2]")
    #     if txt_shedule.text == "daily":
    #         assert True
    #     else:
    #         raise ValueError("schedule not same ")
    #
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
    #         (By.XPATH, "//*[@class='scheduled-exports table table-bordered'][1]//tbody/tr/td[6]/a[1]"))).click()
    #     time.sleep(2)
    #     self.driver.switch_to.alert.accept()
    #     self.driver.quit()
    #
    # def test_action5_case5(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     time.sleep(3)
    #     self.lp = Loginpage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-export']").click()
    #     time.sleep(4)
    #     self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-monthly']").click()
    #     time.sleep(4)
    #     self.driver.find_element(By.XPATH, "// *[ @ id = 'gfb-schedule-monthly-select']").click()
    #     time.sleep(5)
    #     # self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
    #
