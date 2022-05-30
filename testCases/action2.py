from pageObjects.LoginPage import Loginpage
import time
from basetest import BaseTest
from selenium.webdriver.common.by import By
import pytest


class Testaction2(BaseTest):

    def test_action2(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)

        self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[3]/div/button").click()

        time.sleep(1)
        #get export_to_csv
        export_to_csv = self.driver.find_element(By.XPATH, "//*[@class='modal-header']/div")
        validate_export = "Export to CSV"
        try:
            assert export_to_csv.text == validate_export and export_to_csv.is_displayed()
            self.logger.info(f'Passed when validate the export to CSV on the top of modal')
        except Exception as ex:
            self.logger.error(f'Failed when validate the export to CSV on the top of modal '+ {ex})


        #X botton on the right
        x = self.driver.find_element(By.XPATH, "//*[@class='modal-content']//*[@class='modal-header']/button/span[1]")
        try:
            assert x.text == '×' and x.is_displayed()
            self.logger.info(f'Passed when validate the x button on the top right')
        except Exception as ex:
            self.logger.error(f'Failed when validate the x button on the top right '+ {ex})

        #assign to and status
        label_assign = self.driver.find_element(By.XPATH, "//*[@class='form-group col-lg-2 col-md-2 col-12'][1]/label")
        assign_to = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div/div[1]")
        full = f'{label_assign.text}: {assign_to.text}'
        assign_to_modal = self.driver.find_element(By.XPATH, "//*[@class='FiltersBlock-sc-1i0yauu QxZBX']/span[1]")
        try:
            assert assign_to_modal.text == full
            self.logger.info(f'Passed when validate the Assign to users')
        except Exception as ex:
            self.logger.error(f'Failed when validate the Assign to users '+ {ex})

        label_status = self.driver.find_element(By.XPATH, "//*[@class='form-group col-lg-2 col-md-2 col-12'][2]/label")
        status = self.driver.find_element(By.XPATH, "//*[@id='status']/div[1]/div[1]/div[1]/div[1]")
        full = f'| {label_status.text}: {status.text}'
        status_modal = self.driver.find_element(By.XPATH, "//*[@class='FiltersBlock-sc-1i0yauu QxZBX']/span[2]")

        try:
            assert status_modal.text == full
            self.logger.info(f'Passed when validate the status')
        except Exception as ex:
            self.logger.error(f'Failed when validate the status '+ {ex})

        # check run export now: default
        export = self.driver.find_element(By.XPATH, "//*[@id='gfb-run-export-now']")
        try:
            assert export.is_selected()
            self.logger.info(f'Passed when validate the run export now:it should be selected by default')
        except Exception as ex:
            self.logger.error(f'Failed when validate the run export now:it should be selected by default '+ {ex})
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-export']").click()

        # check daily radio button: default
        daily = self.driver.find_element(By.XPATH, "//*[@id='gfb-schedule-daily']")
        try:
            assert daily.is_selected()
            self.logger.info(f'Passed when validate the daily radio button:selected default')
        except Exception as ex:
            self.logger.error(f'Failed when validate the daily radio button:selected default' + {ex})

        self.driver.find_element(By.XPATH, "//*[@class='modal-body']/form/div[4]/input").click()

        #elemnt button with element
        day = self.driver.find_elements(By.XPATH, "//*[@class='Weekdays-sc-1belszz fGPixO']/div/span")
        ar = []
        for days in day:
            ar.append(days.text)
        try:
            assert "Sun" and "Mon" and "Tue" and "Wed" and "Thu" and "Fri" and "Sat" in ar
            self.logger.info(f'Passed when validate the weekly on the following day radio')
        except Exception as ex:
            self.logger.error(f'Failed when validate the weekly on the following day radio' + {ex})

        #day of month
        day_month = self.driver.find_element(By.XPATH, "//*[@class='form-check'][3]/span")
        check_ = "Monthly on the\n1\nof each month"
        try:
            assert day_month.text == check_
            self.logger.info(f'Passed when validate the monthly on each month')
        except Exception as ex:
            self.logger.error(f'Failed when validate the monthly on each month' + {ex})

        #quartely on the days of month
        quartely = self.driver.find_element(By.XPATH, "//*[@class='form-check'][4]/span")
        check_ = "Quarterly on the\n1\nof the following each quarter"
        try:
            assert quartely.text == check_
            self.logger.info(f'Passed when validate the quaterly on each month')
        except Exception as ex:
            self.logger.error(f'Failed when validate the quaterly on each month' + {ex})

        # get Delivery Method text
        delivery_text = self.driver.find_element(By.CLASS_NAME, "mt-3")
        try:
            assert delivery_text.text == "Delivery Method"
            self.logger.info(f'Passed when validate for text delivery method')
        except Exception as ex:
            self.logger.error(f'Failed when validate for text delivery method' + {ex})


