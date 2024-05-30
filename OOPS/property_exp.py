

class Details:

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    def setAge(self,age):
        self.age=age
    
    pro=property(getName,setName)
d=Details()

d.pro="ajk"

print(d.pro)
