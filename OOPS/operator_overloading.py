class Sample:


    def __init__(self,value):
        self.value = value


    def __add__(self,b):
        return a.value+b.value


class DerivedSample(Sample):

    def __init__(self,value) :
        super().__init__(value)

    def getvalue(self):
        return self.value


class DerivedSample2(Sample):
    def __init__(self,value):
        super().__init__(value)




a=DerivedSample(1)
b=DerivedSample2(2)

print(a.value)
print(b.value)

print(a+b)


def func(a,b, c=0):
    print(a+b+c)

def main():

    func(4,5)
    func(4,5,6)
    

if __name__=="__main__":
    main()








