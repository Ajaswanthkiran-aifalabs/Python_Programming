

dt={

    "name":"AJK",
    "age": 20,
    "clg":"KLU",
    "phone No": 908767808,
}




for key,value in dt.items():

    if key=="age" and value<18:
        print("Minor")
    elif key=="age" and value>=18:
        print("Major")
    else:
        print("Age key is not present")
    
def isPrime(num):

    if num<0:
        return False
    
    for i in range(num):

        if num%i==0:
            return False
    
    return True


def main():

    lst=[i for i in range(1,10)]

    for i in lst:
      
        if isPrime():
            print(f"{i} is a prime number")

        

if __name__=="__main__":
    main()