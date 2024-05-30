

def first(fu):

    def inner():
        a=fu()
        return 2*a
    return  inner


def second(fu):

    def inner():
        a=fu()

        return a*a

    return inner




@second
@first
def func():
    return 10

def main():

    print(func())

if __name__=="__main__":
    main()