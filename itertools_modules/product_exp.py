

from itertools import product


def main():


    """Given only A values and repeat is used for iterate itself"""
    # a=product([1,2],repeat=2)
    # print(list(a))

    a=product([1,2],[3,4],repeat=2)
    print(list(a))


if __name__=="__main__":
    main()