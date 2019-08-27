from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from ZBase_Framework.Utilities.Loghandler import Logging
import logging
from ZBase_Framework.Utilities.DataRead_writefile import Excel
import ZBase_Framework.Utilities.ConfigFile as drivepath

#driver = webdriver.Chrome(executable_path=r'E:\\Testing\Drivers\\chromedriver.exe')
#driver.maximize_window()

'''chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--start-maximized")
chrome_options.binary_location= ''

driver = webdriver.Chrome(chrome_options=chrome_options)'''




class Utilities(Logging,Excel):


    def __init__(self):
        Logging()

        wb,sh = Excel(1,1)
        logging.info("====================Test started===========================")
        logging.info("Constructor initialise to call self variables")


# Launching an Browser Using Web driver
    def browserlaunch(self,browsername):
        self.drowsername = browsername
        #path = application_path()
        try:
            if self.drowsername == "Chrome":
                logging.info("Launching Browser- Success: " + self.drowsername)
                self.driver = webdriver.Chrome(executable_path=drivepath.chromedriverpath)
                driver = self.driver
                driver.maximize_window()
                #driver.close()
            else:
                pass
        except:
            logging.info("Unable to Load driver for the browser")
            return driver

    def Openurl(self,enterurl):
        self.urlentr = enterurl
        try:
            self.driver.get(self.urlentr)
            logging.info("Opening URL success: " + self.urlentr)
        except:
            logging.info("Unable to Launch URL")

    def WebLocator_get(self,ObjectId):
        self.locator = ObjectId
        try:
            weblocator = self.locator.split('=')
            if weblocator[0] == "XPath":
                retlocator = self.driver.find_element_by_xpath(weblocator[1])
            elif weblocator[0] == "Id":
                retlocator = self.driver.find_element_by_id(weblocator[1])
            else:
                print("object was not taken correctly failed to retirew")
                pass
        except:
            logging.info("unable to find the weblocator provided from the data sheet plz check weblocator")
            self.driver.close()
        return retlocator

    def Operation_WebLocator(self,Entervalue):
        retlocator = Utilities.WebLocator_get(self,self.locator)
        self.Entervalue = Entervalue
        try:
            retlocator.send_keys(self.Entervalue)
            logging.info("Element Located and value Entered : " + self.Entervalue)
        except:
            logging.info("Unable to locate element: ")
            self.driver.close()

    def initialwebdriver(self):
        return self.driver

if __name__ == "__main__":
    new = Utilities()
    new.browserlaunch("Chrome")
    new.Openurl("http://newon.docagent.net")
    new.WebLocator_get("XPath=//input[contains(@id,'txtUserID')]")
    new.Operation_WebLocator("admin")

