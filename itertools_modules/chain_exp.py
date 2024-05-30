from itertools import chain


def main():

    lst=[1,2,4,5,6]
    lst2=[64,3,32,3,23]
    a=chain(lst,lst2)

    print(list(a))
    


if __name__=="__main__":
    main()