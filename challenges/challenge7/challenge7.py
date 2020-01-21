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

    def test_copart_makes_models_section(self):
        makeModelName = []
        hrefURL = []

        self.driver.get("https://www.copart.com/")

        # get all the elements under Makes/Models section of copart
        makesModelsElems = self.driver.find_elements_by_xpath("//li[starts-with(@ng-repeat,'popularSearch in popularSearches')]/a")

        # get the name value displayed on the page into a list
        for nameValue in makesModelsElems:
            makeModelName.append(nameValue.get_attribute("text"))

        # get the URL for that link into a list
        for hrefValue in makesModelsElems:
            hrefURL.append(hrefValue.get_attribute("href"))

        # strip the '-' characters, some of the names had them
        stripped_Urls = [j.replace('-', ' ') for j in hrefURL]

        # verify the elements navigate to the correct page
        idx = 0
        for item in stripped_Urls:
            parts = item.split("/")
            self.assertEqual(parts[5], makeModelName[idx].lower())
            # print out info below to demonstrate verification
            # print(parts[5] + ' ' + makeModelName[idx].lower())
            if parts[5] in str(makeModelName[idx].lower()):
                print(str(makeModelName[idx]) + "--> The URL is good.")
            else:
                print(str(makeModelName[idx]) + "--> There might be a problem with the URL.")
            idx += 1


        #time.sleep(5)


if __name__ == '__main__':
    unittest.main()
