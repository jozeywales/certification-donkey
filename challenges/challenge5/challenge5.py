import unittest
from cmath import e
from selenium import webdriver
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
        searchElement.send_keys("PORSCHE" + Keys.ENTER)

        ddElement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='serverSideDataTable_length']/label/select")))

        select_list = WebDriverSelect(ddElement)
        select_list.select_by_index()
        selected_option = select_list.deselect_by_index(2)

        porscheModelList = []

        # 1. Find all the models of Porsche
        searchPorscheModels = self.driver.find_elements_by_xpath(
            "//span[@data-uname='lotsearchLotmodel']/../span/text()")

        for element in searchPorscheModels:
            porscheModelList.append(element)

        print(porscheModelList)


if __name__ == '__main__':
    unittest.main()
