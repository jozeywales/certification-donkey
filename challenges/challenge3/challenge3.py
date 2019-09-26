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

        # 1. Find the popular search links
        try:
            childSearchElements = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@href,'./popular/m')]"))
        )
        except TimeoutError:
            print("an exception occurred" + e)

        for element in childSearchElements:
            link = element.get_attribute("href")
            text = element.get_property("text")
            print(text + ' ' + link)



if __name__ == '__main__':
    unittest.main()
