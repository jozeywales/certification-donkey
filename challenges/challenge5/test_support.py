from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select as WebDriverSelect

class SupportCh5():
    '''A class that contains supporting methods for Challenge5 tests.'''
    def __init__(self, driver):
        '''initialize'''
        self.driver = driver
        self.i = 0

    def launchSite(self, url):
        '''Launches a site at the "url" param'''
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.url_contains(url)
            )
        except (Exception) as e:
            print("Error occurred:", e)

    def search_init(self, searchToken):
        '''
        Performs a search on a site with 'searchToken' in the search control
        '''
        try:
            searchElement = self.driver.find_element(By.ID, "input-search")
            searchElement.send_keys(searchToken)
            searchButton = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
            return searchButton.click()
        except (Exception) as e:
            print("Error occurred:", e)


    def setShowEntries(self, value):
        try:
            ddElement = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='serverSideDataTable_length']//select[@name='serverSideDataTable_length']")))
            select_list = WebDriverSelect(ddElement)
            selected_option = select_list.select_by_value('100')
            return select_list, selected_option
        except (Exception) as e:
            print("Error occurred:", e)

    def findModels(self):
        try:
            element = searchPorscheModels = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//td//span[@data-uname='lotsearchLotmodel']")))
            return element
        except (Exception) as e:
            print("Error occurred:", e)

    # the methods that are called from countDamages based on the switcher dictionary
    def rearEnd(self):
        return "REAR END"

    def frontEnd(self):
        return "FRONT END"

    def minorDent_Scratches(self):
        return "MINOR DENT/SCRATCHES"

    def underCarriage(self):
        return "UNDERCARRIAGE"

    def misc(self):
        return "misc"

    # the switcher dictionary is the foundation for what methods to call
    switcher = {
        0: rearEnd,
        1: frontEnd,
        2: minorDent_Scratches,
        3: underCarriage,
        4: misc
    }

    # loop through the VALUES of the passed-in dictionary and call the
    # corresponding method with the key from the dict get() method.
    def countDamages(self, damageTypes):
        for x in damageTypes.values():
            result = self.switcher.get(x)(self)
            if result == "misc":
                print("misc count")
            elif result == "FRONT END":
                print("FRONT END")
            elif result == "REAR END":
                print("REAR END")
            elif result == "MINOR DENT/SCRATCHES":
                print("MINOR DENT/SCRATCHES")
            elif result == "UNDERCARRIAGE":
                print("UNDERCARRIAGE")

    print("   ***   That is all!   ***   ")


