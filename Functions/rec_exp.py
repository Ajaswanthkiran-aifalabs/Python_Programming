

def funA(n):

    if n==0:
        return 0
    else:
        return n+funA(n-1)


def main():
    print(funA(5))


if __name__=="__main__":
    print(type(main))

    main()



