

from itertools import starmap



def main():

    lst=[(1,23,4,5),(345,4,2,3),(453,32,2),(3,23,23,4)]
    a=starmap(max,lst)
    print(list(a))

if __name__=="__main__":
    main()
