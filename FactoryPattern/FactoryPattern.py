import ConfigParser
import datetime
"""
Author : Amitabh Sharma
Basic Logger trying to demonstrate Factory Pattern in Python.
ConsoleLogger, FileLogger classes implement a method log which can be determined by reading a Loggerproperties.ini
file.
This can be further extended to a DBLogger()
"""


class DateClass(object):
        """returns current date and time"""
        @staticmethod
        def getcurrentdate():
                return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class ConsoleLogger(object):
        """Log All the messages on the console"""
        def log(self,msg):
                print "{0} : {1} \r".format(DateClass.getcurrentdate(), msg)


class FileLogger(object):
        """Log all the messages to the file"""
        def log(self,msg):
                with open("Logger.log", "a") as myfile:
                        myfile.write(DateClass.getcurrentdate() + " :  " + msg)


class LogFactory(object):
        def shouldlogtofile(self):
                config = ConfigParser.RawConfigParser()
                config.read("Loggerproperties.ini")
                return config.getboolean("LoggerProperties","logToFile")
        def getLogger(self):
                if(self.shouldlogtofile()):
                        return FileLogger()
                else:
                        return ConsoleLogger()

if __name__ == '__main__':
        logger = LogFactory().getLogger()
        logger.log("Hello World")
