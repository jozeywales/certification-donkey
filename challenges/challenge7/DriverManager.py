from selenium import webdriver
from selenium.webdriver.common import desired_capabilities


class DriverManager():

    def getDriver(self, browser, mobileType=''):

        caps = {}

        if browser == None:
            browser = 'chrome'
        print(browser.lower())

        if browser.lower() == 'chrome' and mobileType == '':
            caps = desired_capabilities.DesiredCapabilities.CHROME
            # caps["browserName"] = browser
            # caps["platform"] = 'WINDOWS'
            # caps["version"] = '10'
            self.driver = webdriver.Chrome(desired_capabilities=caps)

        if browser.lower() == 'firefox' and mobileType == '':
            caps = desired_capabilities.DesiredCapabilities.FIREFOX
            self.driver = webdriver.Firefox(desired_capabilities=caps)

        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        #driver = builder.build()

        if mobileType == '':
            # maximizing chrome browser
            self.driver.maximize_window()

        return self.driver
