from selenium import webdriver
from selenium.webdriver.common import desired_capabilities


class DriverManager():

    def getDriver(self, browser, mobileType):


        if browser == None:
            browser = 'chrome'
        print(browser.lower())

        if browser.lower() == 'chrome' and mobileType == None:
            #caps = {"browserName": "chrome"}
            caps = desired_capabilities.DesiredCapabilities.CHROME
            caps['browserName'] = browser
            caps['platform'] = 'WINDOWS'
            caps['version'] = '10'

        driver = webdriver.Remote(desired_capabilities=caps)

        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        #driver = builder.build()


        if mobileType == None:
            # maximizing chrome browser
            driver.maximize_window()

        return driver
