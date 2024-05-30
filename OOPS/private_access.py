

class FunA:

    def __init__(self):
        self.__a=1
        self._a=1

class FunB(FunA):
    pass

funb=FunB()

print(funb._a)
print(funb.__a)