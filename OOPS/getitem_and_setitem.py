from collections import namedtuple
Student = namedtuple("Student", ('name', 'age'))

class Course:

    def __init__(self, title):
        self.title = title
        self._students = []
        
    def add_student(self, student):
        self._students.append(student)
        
    def __getitem__(self,key):
        return getattr(self,key)
    
    def __setitem__(self,key,value):
        return setattr(self,key,value)
        


c=Course("AJK")

print(c["title"])