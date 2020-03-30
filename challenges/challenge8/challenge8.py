import unittest
import requests
from requests import request
from selenium import webdriver
from driver_manager import DriverManager

class Challenge8():
    url = "https://www.copart.com/public/lots/search"
    payload = {'query':'f150'}
    headers = {'cookie':'s_fid=3502CD421F425097-24E060AD0836DA18; s_vi=[CS]v1|2F186AFF0515E3A9-60000A1EC229E3B8[CE]; OAID=81383f5a76a6e37b1908f24e0e44278e; _gcl_au=1.1.2000596723.1580258815; _fbp=fb.1.1580258815366.2145530811; _ga=GA1.2.1824465011.1580258815; __gads=ID=8d18c64f559595d4:T=1580258814:S=ALNI_MZSyCwNAjnBirqC-0nR7IngSf0EMw; visid_incap_242093=ykaZq2sjRP2CwGeQPvbn5FzJaV4AAAAAQUIPAAAAAAD/AjENPf8ZzqW5U2Co8019; __cfduid=db247d4cb4e014e399871f058bd7941c01583991148; userLang=en; copartTimezonePref=%7B%22displayStr%22%3A%22MDT%22%2C%22offset%22%3A-6%2C%22dst%22%3Atrue%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; timezone=America%2FDenver; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22Utah%22%2C%22stateCode%22%3A%22UT%22%2C%22cityName%22%3A%22Salt%20Lake%20City%22%2C%22latitude%22%3A40.76078%2C%22longitude%22%3A-111.89105%2C%22zipCode%22%3A%2284081%22%2C%22timeZone%22%3A%22-06%3A00%22%7D; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; s_ppvl=public%253Ahomepage%2C35%2C20%2C841%2C1764%2C303%2C1920%2C1080%2C1%2CP; s_ppv=member%253AsearchResults%2C100%2C12%2C2964%2C795%2C874%2C1920%2C1080%2C1%2CL; s_pv=member%3AsearchResults; s_nr=1585543760084-Repeat; s_vnum=1586583135021%26vn%3D7; s_invisit=true; s_lv=1585543760088; s_lv_s=Less%20than%207%20days; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmember%25253AsearchResults%2526link%253DSearch%2526region%253Dsearch-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmember%25253AsearchResults%2526pidt%253D1%2526oid%253DSearch%2526oidt%253D3%2526ot%253DSUBMIT; g2usersessionid=2ff864dcce26b9b21edfdc6f04588403; G2JSESSIONID=6304F04E04B78524858EA43C36932DE1-n2; incap_ses_210_242093=wibHXcqUKT1Ej4Yr8RHqAlF6gV4AAAAAs9CKja283Op1AArrO2WZ9g=='}

    response = requests.request("POST", url, headers=headers, data=payload)

    response_json = response.json()

    # print("Dict key-value are : ")
    # for i in enumerate(response_json.items()):
    #     print(i)

    # using loops to Pretty Print
    print("The Pretty Print dictionary is : ")
    for sub in response_json:
        print(sub)
        for sub_nest in response_json[sub]:
            print(sub_nest, ':', response_json[sub][sub_nest])

    print('***Done!***')
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

