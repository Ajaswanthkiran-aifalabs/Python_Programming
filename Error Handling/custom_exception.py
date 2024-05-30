
class NotEvenListError(Exception):
    pass

def some():
    try:
        raise TypeError("Sample error")
    except TypeError as t:
        print(t)

def main():

    l=[1,2,3,4,6]

    try:

        for i in l:
            if i%2!=0:
                raise NotEvenListError("The list contains odd numbers")
    except NotEvenListError as e:
        print(e)

if __name__=="__main__":
    main()
