import datetime

__author__ = 'amit'
""" Implement Singleton patter in python. Using the same Logging example as FactoryPattern
"""


class DateClass(object):
        """returns current date and time"""
        @staticmethod
        def getcurrentdate():
                return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class FileSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FileSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, msg):
        with open("Logger.log", "a") as myfile:
                myfile.write(DateClass.getcurrentdate() + " :  " + msg)

if __name__ == '__main__':
    instance1 = FileSingleton()
    instance2 = FileSingleton()
    print("id(instance1) = " + str(id(instance1)))
    print("id(instance2) = " + str(id(instance2)))
    assert id(instance1) == id(instance2)