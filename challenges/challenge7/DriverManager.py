from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ie


class DriverManager():

    def getDriver(self, browser='', mobileType=''):

        caps = {}

        browserList = {
            "chrome": "",
            "firefox": "",
            "opera": "",
            "internet explorer": "",
            "microsoftedge": ""
        }

        if browser.lower() not in browserList:
            browser = 'chrome'
        print(browser.lower())

        if browser.lower() in browserList and mobileType == '':
            browserVen = str(browserList[browser]).upper()
            caps = desired_capabilities.DesiredCapabilities.CHROME
            # caps["browserName"] = browser
            # caps["platform"] = 'WINDOWS'
            # caps["version"] = '10'
            self.driver = webdriver.Chrome(desired_capabilities=caps)

        if browser.lower() == 'firefox' and mobileType == '':
            caps = desired_capabilities.DesiredCapabilities.FIREFOX
            self.driver = webdriver.Firefox(".\\browserdrivers", desired_capabilities=caps)

        if browser.lower() == 'internet explorer':
            caps = desired_capabilities.DesiredCapabilities.INTERNETEXPLORER
            caps["platform"] = 'WINDOWS'
            caps["version"] = '10'
            #caps['webdriver.Ie'] = '%USERPROFILE%\\projects\\drivers'
            self.driver = webdriver.Ie('c:\\users\jsteele\\projects\\drivers\\IEDriverServer.exe')

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
