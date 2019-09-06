import HtmlTestRunner
import unittest
import ZBase_Framework.Utilities.ConfigFile as driverpath
import logging

class Results():

    def results(self):
        try:
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=driverpath.Reports))
            print(driverpath.Reports)
        except Exception as e:
            logging.INFO("unable to generate html results "+ e )