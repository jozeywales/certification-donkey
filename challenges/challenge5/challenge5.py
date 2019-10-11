import unittest
from cmath import e
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        searchElement = self.driver.find_element(By.ID, "input-search")
        searchElement.send_keys("PORSCHE")
        searchButton = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
        searchButton.click()

        ddElement = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='serverSideDataTable_length']//select[@name='serverSideDataTable_length']")))

        select_list = WebDriverSelect(ddElement)
        select_list.select_by_value('100')
        selected_option = select_list.first_selected_option.text
        assert selected_option == '100', "The Show dropdown select option is not 100 entries"

        porscheModelList = []

        # 1. Find all the models of Porsche
        searchPorscheModels = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@data-uname='lotsearchLotmodel']/../span")))

        try:
            for element in searchPorscheModels:
                porscheModelList.append(element.text)
        except:
            print(StaleElementReferenceException)

        porscheModelSet = set(porscheModelList)

        print("The number of distinct porsche models is: " + str(len(porscheModelSet)))
        print()




        #for model in porscheModelList:
        #    print(model)


if __name__ == '__main__':
    unittest.main()
