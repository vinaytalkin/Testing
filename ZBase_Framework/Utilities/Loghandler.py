import logging
from datetime import datetime
import sys
import ZBase_Framework.Utilities.ConfigFile as drivepath


class Logging():
    newfilename = ''
    def __init__(self):

        if Logging.newfilename != '':
            LOG_FILENAME = datetime.now().strftime(drivepath.Logfilename)
        #LOG_date_for_file = datetime.now().strftime('E:\\Testing\\Logs\\Test_%H_%M_%S_%d_%m_%Y')
            print(LOG_FILENAME)
            logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
            logging.info("Log File started" + drivepath.Logfilename)
            newfilename = LOG_FILENAME
        else:
            pass

            '''LEVELS = {'debug': logging.DEBUG,
                              'info': logging.INFO,
                              'warning': logging.WARNING,
                              'error': logging.ERROR,
                              'critical': logging.CRITICAL} '''






