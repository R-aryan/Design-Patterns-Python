"""
class containing the sample implementation of
Interface Segregation Principle (ISP)

Basically, the principle is similar to the single responsibility principle
in the sense that classes should only implement methods that they actually use.
"""

from abc import ABC, abstractmethod


class NoTurbo(ABC):
    @abstractmethod
    def __init__(self, name):
        """Please implement intialization of a car"""

    @abstractmethod
    def accelerate(self):
        """Please implement accelerating of a car"""


class WithTurbo(NoTurbo):
    @abstractmethod
    def turbo_accelerate(self):
        """Please implement turboaccelerating of a car"""


class RegularCar(NoTurbo):
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def accelerate(self):
        self.speed += 1
        print("Car %s is accelerating" % self.name)


class SportsCar(WithTurbo):
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def accelerate(self):
        self.speed += 1
        print("Car %s is accelerating" % self.name)

    def turbo_accelerate(self, turbo):
        self.speed += turbo
        print("Car %s is accelerating with turbo %d" % (self.name, turbo))


if __name__ == '__main__':
    car = RegularCar('BMW')
    car.accelerate()

    autoCar = SportsCar('Audi')
    autoCar.turbo_accelerate(2)