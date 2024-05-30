

from itertools import islice



def main():

    lst=[1,2,3,4,5,6,7,8]

    a=islice(lst,4,7)
    print(list(a))






if __name__=="__main__":
    main()
