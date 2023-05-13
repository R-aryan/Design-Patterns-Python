"""
class containing the implementation of liskov Substitution principe.

It should be possible to replace an instance of a superclass with
an instance of a subclass without causing breaking changes.
"""


class Car:
    def __init__(self, name):
        self.name = name
        self.gears = ["N", "1", "2", "3", "4", "5", "6", "R"]
        self.speed = 0
        self.gear = "N"

    def change_gear(self, gear):
        if gear in self.gears:
            self.gear = gear
            print("Car %s is in gear %s" % (self.name, self.gear))

    def accelerate(self):
        if self.gear == "N":
            print("Error: Car %s is in gear N" % self.name)
        else:
            self.speed += 1
            print("Car %s is accelerating" % self.name)


class SportsCar(Car):
    def __init__(self, name):
        super().__init__(name)
        self.turbo = 2

    def accelerate(self):
        if self.gear == "N":
            print("Error: Car %s is in gear N" % self.name)
        else:
            self.speed += self.turbo
            print("Car %s is accelerating with turbo %d" % (self.name, self.turbo))


if __name__ == '__main__':
    # car = Car('BMW')
    # car.changeGear("1")
    # car.accelerate()

    # We can replace Car above with SportsCar without causing breaking changes
    car = SportsCar('BMW')
    car.change_gear("1")
    car.accelerate()
