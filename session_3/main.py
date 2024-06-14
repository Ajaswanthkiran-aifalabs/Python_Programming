

from commands import Commands
from models import PhoneBook


import json

from models import Contact

def read_contacts_from_file(filename):
    with open(filename) as f:
            data=json.load(f)
        
    return data


def copy_to_file(contacts):
        lst=[]

        for i in contacts:
            lst.append({"name":i.name,"phonenumber":i.phone_number})

        with open("phonebook.json","w") as f:
            json.dump({"contacts":lst},f)


def main():

  

    phone_book = PhoneBook()

    
    data = read_contacts_from_file("phonebook.json") 

    for c in data['contacts']:
        phone_book.add_contact(contact=Contact(c['name'],c["phonenumber"]))

    phone_book.add_contact(Contact("AJK","1234567890"))
    
    phone_book.add_contact(Contact("NBK","1234567890"))

    phone_book.add_contact(Contact("AA","1234567890"))

    phone_book.add_contact(Contact("Jaswanth kiran athota","1234567890"))

    phone_book.remove_contact("AA")

    res=phone_book.search_phone_number("12343")
    if res!=None:
        print(f"The contact found! Name: {res.name}  phone number: {res.phone_number}")
    else:
        print("The number is not in the contacts ")
    res=phone_book.search_name("s")

    if res!=None:
        print(f"The contact found! Name: {res.name}  phone number: {res.phone_number}")
    else:
        print("The contact not found!")
    data=phone_book.get_contacts()

    phone_book.display_by_gen()
    copy_to_file(data)


    

    #     command=Commands()

    #     while True:
    #         print("1. Insert\n2. Delete\n3. Search\n4. Display as List\n5. Exit")
    #         c=int(input("Enter your option: "))
    #         print()
        
    #         match c:
    #             case 1:
    #                 name=input("Enter Name: ")
    #                 phone=input("Enter phone number as (123)-456-7890 or 123-456-7890 :")
    #                 command.insert(name,phone)
    #                 print()
    #             case 2:
    #                 name=input("Enter name to delete the contact: ")
    #                 command.delete(name)
    #                 print()
    #             case 3:
    #                 name=input("Enter name to search: ")
    #                 command.search(name)
    #                 print()
    #             case 4:
    #                 print("The list of contacts are: \n")
    #                 command.display()
    #                 print()
    #             case 5:
    #                 command.exit()
    #                 break
    # except Exception as e:
    #     print(e)
if __name__=="__main__":
    main()

    # c=Commands()
    # print("\nDisplaying using generators")
    # c.display_by_gen()
    # print("\nDisplaying using ")
    
