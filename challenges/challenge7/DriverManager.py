from selenium import webdriver
from selenium.webdriver.common import desired_capabilities


class DriverManager():

    def getDriver(self, browser, mobileType=''):

        caps = {}

        if browser == None:
            browser = 'chrome'
        print(browser.lower())

        if browser.lower() == 'chrome' and mobileType == '':
            #caps = {"browserName": "chrome"}
            caps = desired_capabilities.DesiredCapabilities.CHROME
            caps["browserName"] = browser
            caps["platform"] = 'WINDOWS'
            caps["version"] = '10'

        driver = webdriver.Chrome(desired_capabilities=caps)

        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        #driver = builder.build()


        if mobileType == '':
            # maximizing chrome browser
            driver.maximize_window()

        return driver
