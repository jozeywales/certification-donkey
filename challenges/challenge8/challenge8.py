import unittest
import requests
from selenium import webdriver
from driver_manager import DriverManager

class Challenge8():
    response = requests.post('https://www.copart.com/public/lots/search', data={'key':'value'})
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')


    # def Setup(self):
    #     driver_manager = DriverManager(webdriver)
    #     # self.driver = eval(driverManager.getDriver("chrome", "http://www.copart.com"))
    #     self.driver = eval(driver_manager.getDriver("chrome"))
    #     # self.driver = eval(driverManager.getDriver("firefox"))
    #     # self.driver = eval(driverManager.getDriver("ie"))  # doesn't work even after making recommended IE config changes
    #     # self.driver = eval(driverManager.getDriver("opera"))
    #     # self.driver = eval(driverManager.getDriver("edge"))
    #     # self.driver = eval(driverManager.getDriver("safari")) # doesn't work, my laptop is Windows 10
    #     # self.driver = eval(driverManager.getDriver("phantomjs")) # works but message stating to use 'headless' instead
    #
    # def tearDown(self):
    #     self.driver.close()

