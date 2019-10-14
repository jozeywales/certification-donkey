import unittest
from cmath import e

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect
from challenges.challenge5.test_support import SupportCh5


class Challenge5(unittest.TestCase, SupportCh5):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        '''
        This test goes to https://www.copart.com and does a search for "porsche". It then changes
        the drop down for "Show Entries" to 100 from 20. It then counts the number of different
        porsche models in the results of the first page and how many of each type exists.
        '''
        supportCh5 = SupportCh5(self.driver)
        porscheModelList = []

        supportCh5.search_init("porsche")

        select_list, selected_opton = supportCh5.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"


        # 1. Find all the models of Porsche
        results = supportCh5.findModels()
        self.assertTrue(len(results)==100, "The list of Porsche models is not 100")

        for element in results:
            porscheModelList.append(element.text)

        # shortcut to get number of distinct porsche models
        porscheModelSet = set(porscheModelList)

        # count how many of each model
        porscheModelList.sort()
        modelCount = dict()
        for model in porscheModelList:
            modelCount[model] = porscheModelList.count(model)

        print("The number of distinct Porsche models is: " + str(len(porscheModelSet)))
        print("The distinct models are: " + str(porscheModelSet))
        print("The number of each distinct model is: ")
        for x, y in modelCount.items():
            print("{:11s} -> count = {}".format(x, y))


    def test_challenge5_part2(self):
        supportCh5 = SupportCh5(self.driver)
        porscheModelList = []

        supportCh5.search_init("porsche")

        select_list, selected_opton = supportCh5.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        print("   111   ")


if __name__ == '__main__':
    unittest.main()
