
from functools import partial

def multiply(num, times):
    return num*times
    


double=partial(multiply, times=2)

thrice=partial(multiply,times=3)


print(double(3))
