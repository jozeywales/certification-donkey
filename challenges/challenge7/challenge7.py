import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from challenges.challenge6.test_support import SupportCh6


class Challenge7(unittest.TestCase, SupportCh6):

    def setUp(self):
        #driver = driverManager.getDriver("chrome", "http://www.copart.com")
        driver = driverManager.getDriver("chrome", "", "iPhone")
        #driver = driverManager.getDriver("firefox")
        #driver = driverManager.getDriver("internet explorer")
        #driver = driverManager.getDriver("chrome")
        #driver = driverManager.getDriver("CHrOMe")
        #driver = driverManager.getDriver()


    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
