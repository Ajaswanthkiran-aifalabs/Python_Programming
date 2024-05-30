
from typing import Any


def func2(a:str,b:str |1,c: Any):
    pass


def func(a:int,b:int)->int:

    return a+b

def main():

    print(func(1,2))
    print(func2("str",2))
if __name__=="__main__":
    main()