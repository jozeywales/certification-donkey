import time
import unittest
from cmath import e

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect
from challenges.challenge6.test_support import SupportCh6


class Challenge6(unittest.TestCase, SupportCh6):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()

    def test_challenge6p1(self):
        '''
        This is a solution for Challenge 6 I call p1 or part 1. This test first tries to find the
        'SKYLINE' model within the first 100 search results in the try-except-else block after
        doing a general search for the make of 'nissan'. Whether or not the model is found a
        screenShot will be taken. It will then search the entire site including and beyond the
        first 100 search results via the searchAllSite() method and either way will take another
        distinct screenShot.
        '''
        supportCh6p1 = SupportCh6(self.driver)
        modelDesc = "SKYLINE"
        makeDesc = 'Nissan'

        # Search for the make.
        supportCh6p1.search_init(makeDesc)

        select_list, selected_option = supportCh6p1.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        # search for the text 'SKYLINE' in the first 100 models of Nissan.
        try:
            elements = supportCh6p1.findModels100(modelDesc)
        except (TimeoutException) as e:
            print(f"There were no {makeDesc} {modelDesc} models found in the first 100 search results")
            print("Now a search of the entire site will be executed: ")
            self.driver.save_screenshot(modelDesc + "NotFoundScreenShot6sp1.png")
        else:
            print(f"A {makeDesc} {modelDesc} was found in the first 100 search results.")
            self.driver.save_screenshot(modelDesc + "FoundIn100ScreenShot6sp1.png")

        # use the Search control and search all of the site
        srchCntrlLoc = "//div[@id='serverSideDataTable_filter']//input[@type='search']"
        elem = supportCh6p1.getSearchCntrl(srchCntrlLoc)
        elem.send_keys(modelDesc.lower())
        xLocator = "//td//span[@data-uname='lotsearchLotmodel'][starts-with(text(),'SKYLINE')]"
        supportCh6p1.searchAllSite(xLocator, modelDesc)

        print("    ****    ")

    def test_challenge6p2(self):
        '''
        This is a solution for Challenge6 p2 or part 2. It's another variation of searching for
        the 'SKYLINE' model after the initial search for the make of 'nissan'. It looks within
        the first 100 search results only. The try block is a little more detailed than p1 above.
        '''
        supportCh6p2 = SupportCh6(self.driver)
        modelDesc = "SKYLINE"
        makeDesc = "Nissan"

        # Search for the make.
        supportCh6p2.search_init(makeDesc)

        locator = f"//td//span[@data-uname='lotsearchLotmodel'][contains(text(), '{modelDesc}')]"

        # Attempt to find a Skyline model within the 1st 100 search results
        try:
            supportCh6p2.findModels100(modelDesc)
        except (Exception) as e:
            print(f"Could not find a {makeDesc} {modelDesc}: " + str(e))
            self.driver.save_screenshot(modelDesc + "NotFoundScreenShot6sp2.png")
        except (TimeoutException) as e:
            print("A timeout occured: " + str(e))
            self.driver.save_screenshot(modelDesc + "NotFoundScreenShotTimeout6sp1.png")
        else:
            print(f"Yup, I found a {makeDesc} {modelDesc}. Here's a screenshot.")
            self.driver.save_screenshot(modelDesc + "screenshot6p2.png")
        finally:
            print("The 'try-except-else-finally' has finished.")
