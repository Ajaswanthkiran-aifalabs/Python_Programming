

def decfunc(f):


    def efunc(value):
       
        print(value)
       
    return efunc
    




@decfunc
def func(value):
    print("-----In actual function-------")





func(10)