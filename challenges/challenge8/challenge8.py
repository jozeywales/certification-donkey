import requests
import unittest
import logging
import logging.handlers
import os
from selenium import webdriver
from driver_manager import DriverManager


class Challenge8(unittest.TestCase):

    def setUp(self):
        log_dir = "C:\\projects\\certification\\challenges\\challenge8\\logfiles"
        is_accessible = os.access(log_dir, os.F_OK)
        if is_accessible == False:
            os.makedirs(log_dir)
        os.chdir(log_dir)
        f = os.open("p.txt", os.O_RDWR|os.O_CREAT)
        self.handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", log_dir))
        self.formatter = logging.Formatter(logging.BASIC_FORMAT)
        self.handler.setFormatter(self.formatter)
        self.root = logging.getLogger()
        self.root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
        self.root.addHandler(self.handler)

        self.log = logging.getLogger("Challenge8-logger")

    def tearDown(self):
        pass

    def test_query_for_cars_on_copart(self):
        car_query_list = ["toyota camry", "nissan skyline", "Pinto", "Corolla", "F150", "BMW 330xi", "Audi Quatro",
                          "280Z", "International", "Silverado"]

        for car in car_query_list:
            url = "https://www.copart.com/public/lots/search"
            payload = {'query': car}
            headers = {'cookie':'s_fid=3502CD421F425097-24E060AD0836DA18; s_vi=[CS]v1|2F186AFF0515E3A9-60000A1EC229E3B8[CE]; OAID=81383f5a76a6e37b1908f24e0e44278e; _gcl_au=1.1.2000596723.1580258815; _fbp=fb.1.1580258815366.2145530811; _ga=GA1.2.1824465011.1580258815; visid_incap_242093=ykaZq2sjRP2CwGeQPvbn5FzJaV4AAAAAQUIPAAAAAAD/AjENPf8ZzqW5U2Co8019; __cfduid=db247d4cb4e014e399871f058bd7941c01583991148; __gads=ID=8d18c64f559595d4:T=1580258814:S=ALNI_MZSyCwNAjnBirqC-0nR7IngSf0EMw; incap_ses_618_242093=7DkhAvi34HyLIPEoUZSTCE8xjV4AAAAAJoJJPAxR5LwMt+s8qNbyuA==; g2usersessionid=5fbdf2bd9d3db4851a39c669a2c8df33; userLang=en; copartTimezonePref=%7B%22displayStr%22%3A%22MDT%22%2C%22offset%22%3A-6%2C%22dst%22%3Atrue%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; timezone=America%2FDenver; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22Utah%22%2C%22stateCode%22%3A%22UT%22%2C%22cityName%22%3A%22Salt%20Lake%20City%22%2C%22latitude%22%3A40.76078%2C%22longitude%22%3A-111.89105%2C%22zipCode%22%3A%2284081%22%2C%22timeZone%22%3A%22-06%3A00%22%7D; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=b8d4872aca78e4e741920941deb62716; _gid=GA1.2.919308434.1586311530; s_ppvl=public%253Ahomepage%2C65%2C19%2C830%2C707%2C830%2C1920%2C1080%2C1%2CL; s_pv=member%3AsearchResults; s_nr=1586316868149-Repeat; s_vnum=1586583135021%26vn%3D13; s_invisit=true; s_lv=1586316868152; s_lv_s=Less%20than%201%20day; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmember%25253AsearchResults%2526link%253DSearch%2526region%253Dsearch-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmember%25253AsearchResults%2526pidt%253D1%2526oid%253DSearch%2526oidt%253D3%2526ot%253DSUBMIT; s_ppv=member%253AsearchResults%2C65%2C29%2C830%2C707%2C830%2C1920%2C1080%2C1%2CL; G2JSESSIONID=2D3FEBC38A6E3FB2C1095768A54C79C4-n2; incap_ses_210_242093=W1mCZ/GpKCnhfgyB8xHqAkRGjV4AAAAAcK5yUzcbjzpok3JHVoc5pQ=='}

            response = requests.request("POST", url, headers=headers, data=payload)

            # convert serialized json to a dictionary
            response_dict = response.json()

            # grab the value for 'totalElements'
            tot_elements = response_dict['data']['results']['totalElements']
            print(f"Print: The total number of {car}'s found are {tot_elements}")
            self.log.info(f"Log: The total number of {car}'s found are {tot_elements}")
            # print('***Next***')


if __name__ == '__main__':
    unittest.main()


    # if response:
    #     print('Success!')
    # else:
    #     print('Not Found.')


    # def Setup(self):
    #     driver_manager = DriverManager(webdriver)
    #     # self.driver = eval(driverManager.getDriver("chrome", "http://www.copart.com"))
    #     self.driver = eval(driver_manager.getDriver("chrome"))
    #     # self.driver = eval(driverManager.getDriver("firefox"))
    #     # self.driver = eval(driverManager.getDriver("ie"))  # doesn't work even after making recommended IE config changes
    #     # self.driver = eval(driverManager.getDriver("opera"))
    #     # self.driver = eval(driverManager.getDriver("edge"))
    #     # self.driver = eval(driverManager.getDriver("safari")) # doesn't work, my laptop is Windows 10
    #     # self.driver = eval(driverManager.getDriver("phantomjs")) # works but message stating to use 'headless' instead
    #
    # def tearDown(self):
    #     self.driver.close()

