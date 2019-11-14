from selenium import webdriver
from selenium.webdriver.common import desired_capabilities


class DriverManager():

    def getDriver(self, browser='', mobileType=''):

        caps = {}

        # if self.browser.lower() == '':
        #     browser = 'chrome'
        # print(self.browser.lower())

        if browser.lower() == 'chrome' and mobileType == '':
            #caps = desired_capabilities.DesiredCapabilities.CHROME
            caps["browserName"] = browser
            # caps["platform"] = 'WINDOWS'
            # caps["version"] = '10'
            # self.driver = webdriver.Chrome(desired_capabilities=caps)
            temp = self.getWebdriver(browser)
            self.driver = exec(temp)()

        if browser.lower() in 'firefox' and mobileType == '':
            caps = desired_capabilities.DesiredCapabilities.FIREFOX
            self.driver = webdriver.Firefox(desired_capabilities=caps)

        if browser.lower() == 'internet explorer':
            caps = desired_capabilities.DesiredCapabilities.INTERNETEXPLORER
            caps["platform"] = 'WINDOWS'
            caps["version"] = '10'
            #caps['webdriver.Ie'] = '%USERPROFILE%\\projects\\drivers'
            self.driver = webdriver.Ie(desired_capabilities=caps)

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

    def getWebdriver(self, browser_name):
            print("webdriver" + "." + browser_name.title())
            return "webdriver" + "." + browser_name.title()

