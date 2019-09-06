from  ZBase_Framework.Utilities.UIObjects  import Utilities as uiobject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
#-------------------------------------------Locators---------------------
UploadCenter_Archive_Tab = "XPath=//td[contains(@id,'UltraWebTab2td0')]";
mouseoveron_tools = "xpath=/html[1]/body[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/table[1]/tbody[1]/tr[1]/td[1]/a[1]"
movetoelement_upload = "xpath=//a[contains(text(),'Upload Center')]"
selectfolde = "Xpath=/html[1]/body[1]/form[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[3]/div[1]/div[1]/select[1]"
browserdoc = "xpath=//input[@id='UltraWebTab2__ctl0__UploadToArchive1_SourceFile']"
UploadCenter_Archive_Upload = "XPath=//input[contains(@name,'UploadToArchive1:btnUpload')]"
keyfieldsnames = "xpath=//span[contains(@id,'lblKeyType')]"
keyfiled_forall = "//input[@type='text']"


class UploadDoc(uiobject):

    def selecting_Archivetab(self):
        Archive_tab = uiobject.WebLocator_get_element(UploadCenter_Archive_Tab)
        Archive_tab.click()

    def Mouseoveron_Tools(self):
        uiobject.mousehover(mouseoveron_tools,movetoelement_upload)

    def Select_Folder(self,foldername= 'APInvoices'):
        select = uiobject.WebLocator_get_element(selectfolde)
        all_options = [o.get_attribute('value') for o in select.options]
        #for x in all_options:
        select.select_by_value(foldername)
        time.sleep(3)

    def Browse_File(self,filepath = ''):
        path = uiobject.WebLocator_get_element(browserdoc)
        path.send_keys(filepath)

    def Sending_Randomdata_Keyfields(self):
        elements_keyfileds = uiobject.WebLocator_getall_elements(keyfiled_forall)
        elements_keynames = self.driver.find_elements_by_xpath(keyfieldsnames)
        for i in elements_keynames.get_attribute('value'):
            keynamesplt = str(elements_keynames[i].get_attribute('value')).split('(',1)
            if keynamesplt == "String"+")":




