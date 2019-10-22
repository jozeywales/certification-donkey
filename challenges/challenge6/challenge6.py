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

        supportCh6p1 = SupportCh6(self.driver)
        modelDesc = "SKYLINE"

        supportCh6p1.search_init("nissan")

        select_list, selected_option = supportCh6p1.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        # search for the text 'SKYLINE' in the first 100 models of Nissan.
        elements = supportCh6p1.findSkylineModels(modelDesc)

        #self.assertTrue(elements != None, "The Nissan Skyline model was not found.")

        # for model in elements:
        #     if model.text == modelDesc:
        #         print("The model {} was found".format(modelDesc))
        #         break
        #     else:
        #         print("The model {} was NOT found.".format(modelDesc))

        print("    ****    ")

    def test_challenge6p2(self):
        supportCh6p2 = SupportCh6(self.driver)
        modelDesc = "SKYLINE"

        supportCh6p2.search_init("nissan")

        locator = "//*[@id='lot_model_descSKYLINE']"

        try:
            self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException) as e:
            print("Couldn't find the element: " + str(e))
        except (TimeoutException) as e:
            print("A timeout occured: " + str(e))
            supportCh6p2.findSkylineModels(modelDesc)
        else:
            print("In the else clause.")
        finally:
            self.driver.save_screenshot(modelDesc + "screenshot.png")
            print("The 'try except else' has finished.")
