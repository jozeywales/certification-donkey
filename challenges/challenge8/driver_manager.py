from selenium import webdriver
import os


class DriverManager():

    def __init__(self, driver):
        ''''''
        self.driver = driver

    def getDriver(self, browser='', mobileType=''):
        command = ''
        if browser == '':
            browser = 'chrome'

        browser_dict = {
            'chrome': 'webdriver.Chrome(\"chromedriver.exe\")',
            'firefox':'webdriver.Firefox()',
            'ie':'webdriver.Ie(r\"C:\\Users\\jsteele\\projects\\drivers\\IEDriverServer.exe\")',
            'edge':'webdriver.Edge()',
            'opera':'webdriver.Opera()',
            'safari': 'webdriver.Safari()',
            'phantomjs': 'webdriver.PhantomJS()'
        }

        if browser.lower() in browser_dict:
            command = browser_dict.get(browser.lower())
        else:
            print(f"browser {browser} isn't supported.")

        # if mobileType == '':
        #     self.driver.maximize_window()

        return command
        #print("   ***   ")

