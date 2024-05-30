
from dataclasses import dataclass

@dataclass
class Student:

    def __init__(self):
        self._name=""
        self._age=0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name=value

    @property
    def age(self):
        return self._age
    

    @age.setter

    def age(self,value):
        self._age=value


s=Student()


s.name="ajk"

s.age=12

print(s.name,s.age)
