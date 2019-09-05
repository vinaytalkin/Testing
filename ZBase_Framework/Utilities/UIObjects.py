from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from ZBase_Framework.Utilities.Loghandler import Logging
import logging
from ZBase_Framework.Utilities.DataRead_writefile import Excel
import ZBase_Framework.Utilities.ConfigFile as drivepath

#driver = webdriver.Chrome(executable_path=r'E:\\Testing\Drivers\\chromedriver.exe')
#driver.maximize_window()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--start-maximized")
chrome_options.binary_location= ''

try:
    driver = webdriver.Chrome(chrome_options=chrome_options)
except:
    logging.info("pass")

class Utilities(Logging):


    def __init__(self):
        Logging()

        #wb,sh = Excel(1,1)
        logging.info("====================Test started===========================")
        logging.info("Constructor initialise to call self variables")

    # ----------------------#### Launching an Browser ####--------------------------------#
    def browserlaunch(self,browsername):
        self.drowsername = browsername
        logging.info("To Launch URL setting the browser to open :"+ self.drowsername)
        #path = application_path()
        try:
            if self.drowsername == "Chrome":
                try:
                    self.curr_caps = webdriver.DesiredCapabilities.CHROME.copy()
                    self.driver = webdriver.Chrome(executable_path=drivepath.Chromedriverpath)
                    #,desired_capabilities=self.curr_caps
                    logging.info("Broswer launch success")
                    driver = self.driver
                    driver.maximize_window()
                except:
                    logging.info("Unable to launch browser due to some error plZ Chcek driver path need to update")
                    logging.DEBUG("Debug Message")
                    Utilities.close(self)
                    #exit(new)
            elif self.drowsername == "Firefox":
                try:
                    self.driver = webdriver.Firefox(executable_path= drivepath.Firefoxdriverpath)
                    logging.info("Broswer launch success")
                    driver = self.driver
                    driver.maximize_window()
                except:
                    logging.info("Unable to launch browser due to some error plZ Chcek driver path need to update")
                    logging.DEBUG("Debug Message")
            elif self.drowsername == "Ie":
                try:
                    self.driver = webdriver.Ie(executable_path=drivepath.Iedriverpath)
                    logging.info("Broswer launch success")
                    driver = self.driver
                    driver.maximize_window()
                except:
                    logging.info("Unable to launch browser due to some error plZ Chcek driver path need to update")
                    logging.DEBUG("Debug Message")
            elif self.drowsername == "Edgebrowser":
                try:
                    self.driver = webdriver.Edge(executable_path=drivepath.Edgebrowserdriverpath)
                    logging.info("Broswer launch success")
                    driver = self.driver
                    driver.maximize_window()
                except:
                    logging.info("Unable to launch browser due to some error plZ Chcek driver path need to update")
                    logging.DEBUG("Debug Message")
            elif self.drowsername == "Opera":
                try:
                    self.driver = webdriver.Opera(executable_path=drivepath.Operadriverpath)
                    logging.info("Broswer launch success")
                    driver = self.driver
                    driver.maximize_window()
                except:
                    logging.info("Unable to launch browser due to some error plZ Chcek driver path need to update")
                    logging.DEBUG("Debug Message")
            else:
                logging.info("No browser found please check the browser name in correct format")
        except:
            logging.info("Unable to Load driver for the browser")
    # ----------------------#### Sending URL to Browser ####--------------------------------#
    def Openurl(self,enterurl):
        self.urlentr = enterurl
        try:
            self.driver.get(self.urlentr)
            logging.info("Opening URL success: " + self.urlentr)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            logging.info("Unable to Launch URL")
    # ----------------------#### Locating webelement from Browser (ID,Xpath...) ####--------------------------------#
    def WebLocator_get_element(self,ObjectId):
        self.locator = ObjectId

        try:
            #find = str(self.locator).count('=')
            weblocator = self.locator.split('=',1)
            if str(weblocator[0]).lower() == "XPath".lower():
                self.retlocator = self.driver.find_element_by_xpath(weblocator[1])
            elif weblocator[0] == "Id":
                self.retlocator = self.driver.find_element_by_id(weblocator[1])
            else:
                print("object was not taken correctly failed to retirew")
                pass
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            logging.info("unable to find the weblocator provided from the data sheet plz check weblocator")
            Utilities.close(self)
        return self.retlocator
    # ----------------------#### Passing value to element ####--------------------------------#

    def Operation_WebLocator(self,Entervalue):
        self.retlocator = Utilities.WebLocator_get(self,self.locator)
        self.Entervalue = Entervalue
        try:
            retlocator = self.retlocator
            self.retlocator = self.retlocator
            retlocator.send_keys(self.Entervalue)
            logging.info("Element Located and value Entered : " + self.Entervalue)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            logging.info("Unable to locate element: ")
            self.driver.close()
    # ----------------------#### Initialise webdriver ####--------------------------------#
    #def initialwebdriver(self):
        #return self.driver
    # ----------------------#### Close Browser ####--------------------------------#
    def close(self):
        try:
            self.driver.close()
            logging.info("trying to close the browser unable to find the values ")
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            #driver.close()
            logging.info("trying to close the browser unable to find the values ")
    #----------------------#### Locating webelements from Browser (ID,Xpath...) ####--------------------------------#
    #---------taking all count,sort,---------------------
    def WebLocator_getall_elements(self,ObjectId):
        self.elements = ObjectId
        try:
            weblocator = self.locator.split('=')
            if weblocator[0] == "XPath":
                self.retlocator = self.driver.find_elements_by_xpath(weblocator[1])
            elif weblocator[0] == "Id":
                self.retlocator = self.driver.find_elements_by_id(weblocator[1])
            else:
                print("object was not taken correctly failed to retirew")
                pass
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            logging.info("unable to find the weblocator provided from the data sheet plz check weblocator")
            Utilities.close(self)
        return self.retlocator
    # ----------------------#### Screenshot from Page ####--------------------------------#

    # ----------------------#### Mouse Hover ####--------------------------------#
    def mousehover(self,retlocator,):
        self.retlocator = retlocator
        hover = ActionChains(self.driver)
        hover.move_to_element(self.retlocator).perform()
        #hover = ActionChains().move_to_element(self.retlocator)
        #hover.perform()

    # ----------------------#### Scroll down and up ####--------------------------------#





#if __name__ == "__main__":

    #new = Utilities()
    #new.browserlaunch("Chrome")
    #new.Openurl("http://newon.docagent.net")
    #new.WebLocator_get_element("XPath=//input[contains(@id,'txtUserID')]")
    #new.Operation_WebLocator("admin")

