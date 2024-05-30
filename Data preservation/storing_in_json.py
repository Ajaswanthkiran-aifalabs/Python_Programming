
import json


def func(data):

    # print("1.Insert data\n2.Delete Data\n3.Update the phone number\n4.Search by name or phone number")
    
    while True:
        print("1.Insert data\n2.Delete Data\n3.Update the phone number\n4.Search by name or phone number")
    
        c=int(input())
        if c==1:
            name=input("Enter Name: ")
            phone_no=input("Enter Phone number")
            data[name]=phone_no
        elif c==2:
            name=input("Enter name to delete: ")
            del data[name]
        elif c==3:
            name=input("Enter name to update: ")
            phone_no=input("Enter Phone number to update")
            data[name]=phone_no
        elif c==3:
            print("sdgre")
        else:
            break
    with open("sample.json",'w') as f:
        json.dump(data,f)


def main():

    with open("sample.json") as f:
        data = json.load(f)
    
    func(data)


if __name__=="__main__":
    main()