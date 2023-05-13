"""
class containing the sample implementation of
Interface Segregation Principle (ISP)

Basically, the principle is similar to the single responsibility principle
in the sense that classes should only implement methods that they actually use.
"""

from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass