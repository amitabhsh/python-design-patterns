"""
Using deepcopy to test prototype
"""
from copy import deepcopy

__author__ = 'amit'


class Prototype(object):
    def clone(self):
        print "Object Cloned"
        return deepcopy(self)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Employee(Prototype):
    def __init__(self):
        self.name = None
        self.dept = None


if __name__ == '__main__':
    firstemployee = Employee()
    firstemployee.name = 'Amit'
    firstemployee.dept = 'Engineering'
    secondemployee = firstemployee.clone()
    thirdemployee = secondemployee.clone()
    assert id(firstemployee) != id(secondemployee)
    assert id(secondemployee) != id(thirdemployee)
    assert firstemployee == secondemployee == thirdemployee



