#reading the excel files using xlrd, openpyxl(xl, xlsx formats)
import openpyxl
import logging
import ZBase_Framework.Utilities.ConfigFile as drivepath
from ZBase_Framework.Utilities.Loghandler import Logging
import xlutils
from datetime import datetime


class Excel(Logging):

    def __init__(self,excelpath, rowinInt, colinInt):
        Logging()
        logging.info("====================Excel Test started===========================")
        self.excelpath = excelpath
        self.rowinInt = rowinInt  #
        self.colinInt = colinInt
        self.rowval = 1
        self.colval =1
        logging.info("Excel construction was created and inist")


    def xlutils_excelconnection(self):
        row = xlutils.getRowCount(self.excelpath, 'Sheet1')


    def excelconnection(self):
        #path = application_path
        self.wb = openpyxl.load_workbook(drivepath.Excelpath)
        logging.info("connection was success")
        self.sh = self.wb.active
        logging.info("workssheet was active "+ self.sh.title)
        return self.wb,self.sh

    def excelwsheet(self,worksheet):
        #wb, sh = Excel.excelconnection(self)
        self.worksh = worksheet
        self.sheetname = self.wb.get_sheet_names()
        if str(self.sheetname).lower() == self.worksh.lower():
            logging.info("Passed through parmeter worksheet is equal to = "+ self.sheetname)
            sh = self.wb.active
            logging.info("Sheet found :" + self.sheetname)

    def excel_writeResults(self,rowsval, columnsval, enter_value):
        self.val = enter_value
        self.rowvals = rowsval
        self.colvall = columnsval
        #self.sheetname = excelo.excelwsheet(self.worksh)
        row = self.sh.max_row
        col = self.sh.max_column
        self.enterrowval = self.sh.cell(row=self.rowvals, column=self.colvall)
        a = self.enterrowval.value = self.val
        print(a)
        for rows in range(1,row + 1):
            for cols in range(1,col + 1):
                pass

    def save_closeexcel(self):
        wb,sh = Excel.excelconnection(self)
        wb.save(self.excelpath)
        wb.close()







excelo = Excel(drivepath.Excelpath,1,2)
excelo.excelconnection()
excelo.excelwsheet("Sheet1")
excelo.excel_writeResults(2,8,"hello vinay")
excelo.save_closeexcel()









