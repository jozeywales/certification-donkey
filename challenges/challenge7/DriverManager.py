from selenium import webdriver


class DriverManager():

    def __init__(self, driver):
        ''''''
        self.driver = driver

    def getDriver(self, browser='', mobileType=''):
        command = ''

        browser_dict = {
            'chrome':'webdriver.Chrome(\"../chromedriver.exe\")',
            'firefox':'webdriver.Firefox()',
            'internet explorer':'webdriver.Ie(\"%USERPROFILE%\\projects\\drivers\")',
            'microsoftedge':'webdriver.Edge()',
            'opera':'webdriver.Opera()'
        }

        if browser.lower() in browser_dict:
            command = browser_dict.get(browser)

        # if mobileType == '':
        #     self.driver.maximize_window()

        return command
        #print("   ***   ")

        # if browser.lower() == '' or browser.lower == None:
        #     browser = 'chrome'
        #     self.driver = webdriver.Chrome()
        # else:
        #     for browser_type in browser_dict:
        #         if browser.lower() == browser_type:
        #             self.driver = exec(browser_dict[str(browser)])
        #         break



        #caps = {}

        # if browser.lower() == 'chrome' and mobileType == '':
        #     #caps = desired_capabilities.DesiredCapabilities.CHROME
        #     #caps["browserName"] = browser
        #     # caps["platform"] = 'WINDOWS'
        #     # caps["version"] = '10'
        #     self.driver = webdriver.Chrome(desired_capabilities=caps)
        #
        # if browser.lower() in 'firefox' and mobileType == '':
        #     caps = desired_capabilities.DesiredCapabilities.FIREFOX
        #     self.driver = webdriver.Firefox(desired_capabilities=caps)
        #
        # if browser.lower() == 'internet explorer':
        #     caps = desired_capabilities.DesiredCapabilities.INTERNETEXPLORER
        #     caps["platform"] = 'WINDOWS'
        #     caps["version"] = '10'
        #     #caps['webdriver.Ie'] = '%USERPROFILE%\\projects\\drivers'
        #     self.driver = webdriver.Ie(desired_capabilities=caps)
        #
        # if browser.lower() == 'microsoftedge':
        #     caps = desired_capabilities.DesiredCapabilities.EDGE
        #     self.driver = webdriver.Edge(executable_path='c:\\users\jsteele\\projects\\drivers\\MicrosoftWebDriver.exe')
        #
        # if browser.lower() == 'opera':
        #     caps = desired_capabilities.DesiredCapabilities.OPERA
        #     self.driver = webdriver.Opera(desired_capabilities=caps)

        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        #driver = builder.build()


    # def getWebdriver(self, browser_name):
    #         print("webdriver" + "." + browser_name.title())
    #         return "webdriver" + "." + browser_name.title()

