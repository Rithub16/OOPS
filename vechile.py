from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Child Class 1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition")


# Child Class 2
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self-start button")


# Child Class 3
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with heavy-duty diesel ignition")


# Creating Objects
c1 = Car()
b1 = Bike()
bus1 = Bus()

# Calling Methods
c1.start_engine()
b1.start_engine()
bus1.start_engine()
