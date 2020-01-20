import time
import unittest
from selenium import webdriver
from driver_manager import DriverManager


class Challenge7(unittest.TestCase, DriverManager):

    def setUp(self):
        driverManager = DriverManager(webdriver)
        # self.driver = eval(driverManager.getDriver("chrome", "http://www.copart.com"))
        self.driver = eval(driverManager.getDriver("chrome"))
        # self.driver = eval(driverManager.getDriver("firefox"))
        # self.driver = eval(driverManager.getDriver("ie"))  # doesn't work even after making recommended IE config changes
        # self.driver = eval(driverManager.getDriver("opera"))
        # self.driver = eval(driverManager.getDriver("edge"))
        # self.driver = eval(driverManager.getDriver("safari")) # doesn't work, my laptop is Windows 10
        # self.driver = eval(driverManager.getDriver("phantomjs")) # works but message stating to use 'headless' instead


    def tearDown(self):
        self.driver.close()

    def test_launch_duckduckgo(self):
        self.driver.get("https://duckduckgo.com")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
