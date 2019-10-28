from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect


class SupportCh6():

    def __init__(self, driver):
        self.driver = driver

    def search_init(self, searchToken):
        '''
        Performs a search on copart.com site with 'searchToken' in the search control
        '''
        try:
            searchElement = self.driver.find_element(By.ID, "input-search")
            searchElement.send_keys(searchToken)
            searchButton = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
            return searchButton.click()
        except (Exception) as e:
            print("Error occurred:", e)


    def setShowEntries(self, value):
        '''
        Selects the Show Entries drop down control to select and verify the 100 option.
        '''
        try:
            ddElement = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='serverSideDataTable_length']//select[@name='serverSideDataTable_length']")))
            select_list = WebDriverSelect(ddElement)
            selected_option = select_list.select_by_value('100')
            return select_list, selected_option
        except (Exception) as e:
            print("Error occurred:", e)


    def findModels100(self, modelType):
        elements = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, "//td//span[@data-uname='lotsearchLotmodel'and contains(text(), '{}')]".format(modelType))))
        return elements


    def getSearchCntrl(self, xPathString):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xPathString)))
        return element

    def searchAllSite(self, modelLocator, modelToSearch):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, modelLocator)))
        except (NoSuchElementException) as e:
            print(f"There were no models of {modelToSearch} found on the entire site: " + str(e))
            self.driver.save_screenshot(modelToSearch + "notFoundAllSrch6sp1.png")
        else:
            print(f"Found a {modelToSearch} model beyond the first 100 results. Take a screenShot")
            self.driver.save_screenshot(modelToSearch + "foundAllSrch6sp1.png")
