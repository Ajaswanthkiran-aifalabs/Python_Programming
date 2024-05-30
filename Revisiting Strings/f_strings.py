

def main():
    name="ajk"
    age=21
    s=f"Name: {name}\nAge: {age}"
    print(s)

    # format using "=" formate specifier 
    count=0
    for i in range(1,6):

        if i%2==0:
            count+=1
    
    print(f"The even numbers count is: {count}")  # Normal way
    print(f"The even number {count=} ") # using "=" formate specifier 
    

if __name__=="__main__":
    main()