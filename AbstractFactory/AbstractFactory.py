"""
Abstract Factory Pattern
"""
__author__ = 'amit'


class Car(object):
    def make(self):
        print "A Car\n"


class AirPlanes(object):
    def make(self):
        print "An Airplane\n"


class CarFactory(object):
    def get(self):
        return Car()


class AirPlanesFactory(object):
    def get(self):
        return AirPlanes()


class Factory(object):
    def __init__(self, factory=None):
        self.factory = factory

    def get(self):
        return self.factory.get().make()


if __name__ == '__main__':
    build1 = Factory(CarFactory()).get()
    build2 = Factory(AirPlanesFactory()).get()





