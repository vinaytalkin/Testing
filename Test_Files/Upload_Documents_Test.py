from  Test_Repository.Login_Page import Loginpage
from ZBase_Framework.Utilities.Loghandler import Logging
from ZBase_Framework.Utilities.DataRead_writefile import Excel
import ZBase_Framework.Utilities.ConfigFile as drivepath
import logging
import unittest

#Logging()
class Upload_Documents(unittest.TestCase):

    @classmethod
    def setUp(self):
        logging.info("====================Test started===========================")
        logging.info("$$$Login test started")
        row,col,sheet,wb = Excel.excel_sheet(self,'Login','Sheet1')
        #sheet.cell(row = 2,column=1).value = 'new'
        for nooftimes in range(2,row + 1):
            Loginpage.browser_launch(self,sheet.cell(row = nooftimes,column=2).value)
            Loginpage.browser_url(self,sheet.cell(row = nooftimes,column=3).value)
            Loginpage.userid(self,'',sheet.cell(row = nooftimes,column=4).value)
            Loginpage.password(self,'',sheet.cell(row = nooftimes,column=5).value)
            Loginpage.click_login(self)
    def Test_UploadDoc(self):
        pass




    @classmethod
    def tearDownClass(cls):
        print("all execution closes")