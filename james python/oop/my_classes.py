from random import random


class Dog:
    count = 0
    def __init__(self, dog_name, dog_age, dog_color):
        """This class creates Dog Data type"""
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color    
        Dog.count += 1
    
    def bark(self):
        print(f"{self.name} is barking...woof!")
    
    def run(self):
        print(f"{self.name} is runnning...")


class Student:
    COUNT = 0
    def __init__(self, name,age,program):
        self.name = name
        self.age = age
        self.program = program
    
    def enroll(self):
        self.id = int(10 * random())
        Student.COUNT += 1
        print(f"student [{self.name}] is enrolled and here's the STudent ID: {self.id}")
    
    def count(self):
        print(f"Total Number of Students is: {self.COUNT}")
        
        
        
