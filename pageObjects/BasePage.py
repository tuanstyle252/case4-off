import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage():
    driver = None
    logger = None

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger