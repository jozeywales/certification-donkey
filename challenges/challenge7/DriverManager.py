class DriverManager():
    def __init__(self, browser, mobileType):
        self.browser = browser
        self.mobileType = mobileType
    #if (browser == "firefox") {
    # console.log("create a new firefox browser")
    # var driver = new webdriver.Builder()
    # .forBrowser("firefox").build()
    # }
    #if (browser == "internet explorer"){
    # console.log("create a new IExplorer browser")
    # var driver = new webdriver.Builder()
    # .forBrowser("internet explorer").build()
    # } ...

    # var driver = new webdriver.Builder().forBrowser(browser).build()

    #builder = webdriver.Builder()
    # builder.forBrowser("chrome")
    # builder.build()

    # if rm != null:
    #     builder.usingServer(rm)
    def getDriver(self):
        if self.browser == None:
            browser = 'chrome'
        print(self.browser.lower())
        #builder.forBrowser(browser.toLowerCase())

        if self.browser.lower() == 'chrome' and self.mobileType != None:
            caps = {
                browserName: "chrome",
                chromeOptions: {
                    mobileEmuilation: {
                        deviceName: mobileType
                        # deviceName: 'iPhone X'
                    }
                }
            }
        #builder.withCapabilities(caps)
        # const {Options} = require("selenium-webdriver/chrome")
        # builder.setChromeOptions(new Options().setMobileEmulation({deviceName: "iPhone X"}))

        driver = builder.build()

        if mobileType == None:
            # maximizing chrome browser
            driver.manage().window().maximize()

        return driver
