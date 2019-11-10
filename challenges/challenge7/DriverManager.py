from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver import ie


class DriverManager():

    def getDriver(self, browser='', mobileType=''):

        caps = {}

        if browser == '':
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

        if browser.lower() == 'internet explorer':
            #caps = desired_capabilities.DesiredCapabilities.INTERNETEXPLORER
            #caps['webdriver.Ie'] = '%USERPROFILE%\\projects\\drivers'
            self.driver = webdriver.Ie()

        if browser.lower() == 'microsoftedge':
            caps = desired_capabilities.DesiredCapabilities.EDGE
            self.driver = webdriver.Edge(executable_path='c:\\users\jsteele\\projects\\drivers\\MicrosoftWebDriver.exe')

        if browser.lower() == 'opera':
            caps = desired_capabilities.DesiredCapabilities.OPERA
            self.driver = webdriver.Opera(desired_capabilities=caps)

        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        #driver = builder.build()

        if mobileType == '':
            # maximizing chrome browser
            self.driver.maximize_window()

        return self.driver
