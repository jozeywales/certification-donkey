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
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()

    def test_challenge5_part1(self):
        '''
        This test goes to https://www.copart.com and does a search for "porsche". It then changes
        the drop down for "Show Entries" to 100 from 20. It then counts the number of different
        porsche models in the results of the first page and how many of each type exists and
        prints the stats to the console.
        '''
        supportCh5p1 = SupportCh5(self.driver)
        porscheModelList = []
        modelCount = dict()

        supportCh5p1.search_init("porsche")

        select_list, selected_opton = supportCh5p1.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"


        # 1. Find all the models of Porsche
        results = supportCh5p1.findModels()
        self.assertTrue(len(results)==100, "The list of Porsche models is not 100")

        for element in results:
            porscheModelList.append(element.text)

        # shortcut to get number of distinct porsche models
        porscheModelSet = set(porscheModelList)

        # count how many of each model
        porscheModelList.sort()

        for model in porscheModelList:
            modelCount[model] = porscheModelList.count(model)

        print("The number of distinct Porsche models is: " + str(len(porscheModelSet)))
        print("The distinct models are: " + str(porscheModelSet))
        print("The number of each distinct model is: ")
        for x, y in modelCount.items():
            print("{:11s} -> count = {}".format(x, y))


    def test_challenge5_part2(self):
        '''
        This test goes to https://www.copart.com and does a search for "porsche". It then changes
        the drop down for "Show Entries" to 100 from 20. From a switch statement created from a
        dictionary it counts the number of several types of damages and prints those stats to
        the console.
        '''
        supportCh5p2 = SupportCh5(self.driver)
        porscheDamagesList = []

        supportCh5p2.search_init("porsche")

        select_list, selected_opton = supportCh5p2.setShowEntries("100")
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        # 1. get a list of all the porsche models damages elements
        locstring = "//*[@id='serverSideDataTable']//td[12]"
        allDamageElems = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, locstring)))

        # 2. make a list of damages
        for damage in allDamageElems:
            porscheDamagesList.append(damage.text)

        # sort the list
        porscheDamagesList.sort()

        # create a dictionary containing the coded types as values, ie. 1="REAR END", 2="FRONT END",,,
        damageTypesDict = {}
        for x in range(len(porscheDamagesList)):
            if porscheDamagesList[x] == "REAR END":
                type = 0
                damageTypesDict[x] = type
            elif porscheDamagesList[x] == "FRONT END":
                type = 1
                damageTypesDict[x] = type
            elif porscheDamagesList[x] == "MINOR DENT/SCRATCHES":
                type = 2
                damageTypesDict[x] = type
            elif porscheDamagesList[x] == "UNDERCARRIAGE":
                type = 3
                damageTypesDict[x] = type
            else:
                type = 4
                damageTypesDict[x] = type

        # 4. Call/build a switch statement and iterate the list
        supportCh5p2.countDamages(damageTypesDict)

        print("***   That is all.   ***")


if __name__ == '__main__':
    unittest.main()
