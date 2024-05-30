
from itertools import dropwhile


def main():


    lst=[2,5,4,7,5]

    a=dropwhile(lambda x: x%2==0,lst)

    print(list(a))


if __name__=="__main__":
    main()