

from itertools import cycle



def main_list():

    print("Printing list elements using cycle")
    lst=[1,34,23,4,2,"231"]
    
    for j,i in enumerate(cycle(lst)):

        if j==10:
            break

        print(i)

def main(): 
    t=0

    for i in cycle("AJK"):

        if t>8:
            break

        print(i)

        t+=1


def main_next():

    print("Printing each element using next() ")
    c=cycle("qwerty")
    print(next(c))
    print(next(c))
    
if __name__=="__main__":
    main()
    main_list()
    main_next()