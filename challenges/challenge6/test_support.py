from fixtures import TimeoutException
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


    def findSkylineModels(self, modelType):
        try:
            elements = searchPorscheModels = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//td//span[@data-uname='lotsearchLotmodel'and contains(text(), '{}')]".format(modelType))))
            return elements
        except (TimeoutException) as e:
            print("Error occurred: model not found" + ' ' + str(e))

