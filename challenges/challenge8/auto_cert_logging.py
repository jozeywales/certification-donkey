import logging
import logging.handlers
import datetime
import os

class Logger:

    def log_method(self):
        log_dir = "C:\\projects\\certification\\challenges\\challenge8\\logfiles"
        is_accessible = os.access(log_dir, os.F_OK)
        if is_accessible == False:
            os.makedirs(log_dir)
        os.chdir(log_dir)
        file = os.open("chal8.log", os.O_RDWR|os.O_CREAT)
        handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", log_dir + "\\chal8.log"))
        formatter = logging.Formatter(logging.BASIC_FORMAT)
        handler.setFormatter(formatter)
        root = logging.getLogger()
        root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
        root.addHandler(handler)

    # log = logging.getLogger("Challenge8-logger")