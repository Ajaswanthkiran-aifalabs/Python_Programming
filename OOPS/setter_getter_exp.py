

from dataclasses import dataclass


@dataclass
class Student:

    name: str
    age: int
    dept: str

    @property
    def display_details(self):
        print(f"Name: {self.name} \nAge: {self.age}\nDepartment: {self.dept}")

    
s=Student("ajk",20,"CSE")

print(getattr(s,"name"))

setattr(s,'name','a.jaswanth kiran')

print(getattr(s,'name'))