

class Exp:

    def __init__(self,value=0):
        self._value=value

    @property
    def valuefunc(self):
        return self._value
    

    @valuefunc.setter
    def valuefunc(self,value):
        self._value=value



c=Exp()

print(c.valuefunc)

c.valuefunc=49

print(getattr(c,"_value"))