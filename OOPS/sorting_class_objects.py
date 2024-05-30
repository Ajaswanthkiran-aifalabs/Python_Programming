from dataclasses import dataclass

class Student:

    students=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.students.append(self)


    def sort_students(self):
        self.students.sort(key=lambda student: getattr(student,"age"), reverse=True)

    
    def display(self):

        for i in self.students:
            print(i.name,i.age)

    
s=Student("AJK",20)

s1=Student("RAVI",22)
   
s2=Student("MNBVC",21)

s3=Student("QWERTY",10)


s.sort_students()

s.display()