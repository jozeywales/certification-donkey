import os
import unittest
from cmath import e
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Fieldname(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.supportToolsSignIn()

    def tearDown(self):
        self.driver.close()

    def supportToolsSignIn(self):
        print("I'm in the test_supportToolsSignIn method now.")

        support_tools_window = self.driver.window_handles[0]    #get ready to switch tabs

        self.driver.get("https://test-shopdoterra.myvoffice.com/supporttools/index.cfm")
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )

        assert "supporttools" in self.driver.current_url

        #first of 3 pages for supporttools login
        elem = self.driver.find_element(By.NAME,"U_Login_ID")
        elem.click()
        elem.clear()
        elem.send_keys("jsteele")

        elem = self.driver.find_element(By.NAME,"U_Pass")
        elem.click()
        elem.clear()
        elem.send_keys("Lemon123!")

        elem = self.driver.find_element(By.NAME,"U_Name")
        elem.click()
        elem.clear()
        elem.send_keys("John Steele")

        elem = self.driver.find_element(By.NAME,"login")
        elem.click()

        # 2nd of 3 pages for supporttools login
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,"//input[@name='search_value']"))
        )
        elem = self.driver.find_element(By.XPATH,"//div[contains(text(),'User Search')]")
        self.assertEqual("User Search", elem.text, "The User Search container is not displayed")

        elem = self.driver.find_element(By.NAME,"search_value")
        elem.click()
        elem.clear()
        elem.send_keys("4674721")   #wa user id to login with

        elem = self.driver.find_element(By.CSS_SELECTOR,"input[class='ui button']")
        elem.click()
        self.shopdoterraSignIn()
        self.get_new_window(support_tools_window)

    def shopdoterraSignIn(self):
        loginBtnElem = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='Login']"))
        )
        loginBtnElem.click()
        return

    def get_new_window(self, initial_window):
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != initial_window:
                new_window = window
        self.driver.switch_to.window(initial_window)
        assert self.driver.title != "https://test-shopdoterra.myvoffice.com/supporttools/index.cfm", "title should not be 'Essential Oils Pure and Natural | dōTERRA Essential Oils |'"
        WebDriverWait(self.driver.switch_to.window(new_window),30)
        assert self.driver.title == "Essential Oils Pure and Natural | dōTERRA Essential Oils |", "title should be 'Essential Oils Pure and Natural | dōTERRA Essential Oils |'"
        return

    def test_getFieldNameAttr(self):
        print("I'm ready to run the real test now.")
        count = 0
        allElements = self.driver.find_elements_by_xpath("//*")
        #print(os.path.abspath('.')) # C:\projects\certification\challenges\shopdoterra

        with open('./fieldnameElements.txt', 'a') as file_object:
            for element in allElements:
                fieldnameAttr = element.get_attribute("fieldname")
                if str(fieldnameAttr) == "None":    # filter 'None'
                    continue
                href =  element.get_attribute("href")
                #tagName = element.tag_name
                count += 1
                file_object.write(str(count) + ". " + "fieldname attribute = " + str(fieldnameAttr) + ' '
                                  + "href = " + str(href) + "\n")
            file_object.close()

        return




if __name__ == '__main__':
    unittest.main()
