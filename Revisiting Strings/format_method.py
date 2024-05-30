

def main():

    #positional arguments 
    print("Name:{0}\nAge: {1}".format("AJK","21"))


    # Keyword Arguments
    print("Name: {name}\nAge: {age}".formate(age=21,name="ajk"))

    #main use of format method
    s="Name: {name}\nAge :{age}"

    print(s.format(name="ajk",age=21)) # we can provide the values when we want to print

if __name__=="__main__":
    main()

