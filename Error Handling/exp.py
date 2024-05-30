


def main(a,b):

    try:
        c=a/b
        print(c)
        
    except ZeroDivisionError:
        print("error")
    else:
        print("else block")
    finally:
        print("finally")
    




if __name__=="__main__":
    main(5,3)