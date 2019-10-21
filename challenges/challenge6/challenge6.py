import time
import unittest
from cmath import e

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect
from challenges.challenge6.test_support import SupportCh6


class Challenge6(unittest.TestCase, SupportCh6):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):

        supportCh6 = SupportCh6(self.driver)

        supportCh6.search_init("nissan")

        select_list, selected_opton = supportCh6.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        

        time.sleep(10)

