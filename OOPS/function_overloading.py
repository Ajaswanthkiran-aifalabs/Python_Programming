

from multipledispatch import dispatch




@dispatch(int,int)
def fun(a,b):
    print(a+b)

@dispatch(int,int,int)
def fun(a,b,c):
    print(a+b+c)

def main():

    
    fun(1,2)
    fun(1,2,3)


if __name__=="__main__":

    main()