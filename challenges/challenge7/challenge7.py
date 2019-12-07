import time
import unittest
from selenium import webdriver
from challenges.challenge7.DriverManager import DriverManager


class Challenge7(unittest.TestCase, DriverManager):

    def setUp(self):
        driverManager = DriverManager(webdriver)
        # self.driver = eval(driverManager.getDriver("chrome", "http://www.copart.com"))
        self.driver = eval(driverManager.getDriver("chrome"))
        # self.driver = eval(driverManager.getDriver("firefox"))
        # self.driver = eval(driverManager.getDriver("ie"))
        # self.driver = eval(driverManager.getDriver("opera"))
        # self.driver = eval(driverManager.getDriver("edge"))
        # self.driver = eval(driverManager.getDriver("safari"))
        # self.driver = eval(driverManager.getDriver("phantomjs"))


    def tearDown(self):
        self.driver.close()

    def test_launch_duckduckgo(self):
        self.driver.get("https://duckduckgo.com")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
