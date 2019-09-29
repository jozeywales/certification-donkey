import unittest
from cmath import e
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        # 1. Find the popular search captions and links
        try:
            childSearchElementsMakesModels = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@href,'./popular/m')]"))
        )
        except TimeoutError:
            print("an exception occurred" + e)

        print("Makes/Models")
        for element in childSearchElementsMakesModels:
            link = element.get_attribute("href")
            text = element.get_property("text")
            print(text + ' ' + link)

        self.assertCountEqual(str(len(childSearchElementsMakesModels)),"20","The count of Makes/Models is not 20")

        # 2. Find the Categories captions and links
        try:
            childSearchElementsCategories = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='tabTrending']/div[3]//a"))
        )
        except TimeoutError:
            print("an exception occurred" + e)

        i = 0
        print("\nCategories")
        while i < len(childSearchElementsCategories):
            print(childSearchElementsCategories[i].text + " " + str(childSearchElementsCategories[i].get_attribute("href")))
            i += 1

        self.assertCountEqual(str(len(childSearchElementsCategories)),"20","The count of Categories is not 20")


if __name__ == '__main__':
    unittest.main()
