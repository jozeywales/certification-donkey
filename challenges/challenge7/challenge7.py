import time
import unittest
from selenium import webdriver
from challenges.challenge7.DriverManager import DriverManager


class Challenge7(unittest.TestCase, DriverManager):

    def setUp(self):
        driverManager = DriverManager(webdriver)
        # self.driver = driverManager.getDriver("chrome", "http://www.copart.com")
        self.driver = driverManager.getDriver('chrome')
        # self.driver = driverManager.getDriver("firefox")
        # self.driver = driverManager.getDriver("internet explorer")
        # self.driver = driverManager.getDriver("opera")
        # self.driver = driverManager.getDriver()
        # self.driver = driverManager.getDriver("MicrosoftEdge")

    def tearDown(self):
        self.driver.close()

    def test_launch_duckduckgo(self):
        self.driver.get("https://duckduckgo.com")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
