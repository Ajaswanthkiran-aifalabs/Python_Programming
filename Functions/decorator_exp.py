

def fence(func):
    
    def inner_log(val):
        print("*"*10)
        func(val)
        print("*"*10)
    return inner_log



@fence
def log(val):
    print(val)

def  main():

    log(5)

if __name__=="__main__":
    main()