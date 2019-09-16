import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        #self.driver.find_element(By.ID, "input-search")
        searchelement = self.driver.find_element(By.ID, "input-search")
        searchelement.send_keys("exotic" + Keys.ENTER)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'PORSCHE')]"))
            )
        except TimeoutError:
            print("A timeout occurred.")
        finally:
            assert ("PORSCHE" in element[0].text), "No rows containing text 'PORSCHE' found."


if __name__ == '__main__':
    unittest.main()


