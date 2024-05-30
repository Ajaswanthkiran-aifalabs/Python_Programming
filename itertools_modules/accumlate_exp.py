
from itertools import accumulate

import operator


def func(lst):

    return lst*2

def main():


    a=accumulate([1,2,3,4,5])

    print(list(a))

    b=accumulate([1,2,3,4,5],func)

    print(list(b))

if __name__=="__main__":

    main()