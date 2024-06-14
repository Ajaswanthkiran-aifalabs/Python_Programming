

from itertools import count


def main_next():

    c=count(0,10)

    print(next(c))
    print(next(c))


def main():

    for i in count(0):

        if i>100:
            break

        print("Heehee ",i)


if __name__=="__main__":
    print(__name__)
    main()
    main_next()

