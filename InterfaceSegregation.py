'''The “I” in SOLID is for Interface Segregation Principle, which states that clients should not be forced
 to depend on methods they don’t use. If a class exposes so many members that those members can be broken 
 down into groups that serve different clients that don’t use members from the other groups, you should think
 about exposing those member groups as separate interfaces.'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')

#design which adheres interface segregation Principle
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")
