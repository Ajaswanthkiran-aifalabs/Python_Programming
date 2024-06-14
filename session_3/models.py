

import json

from validators import check

class Contact():
    def __init__(self, name: str, phone_number: str):
        self.name=name
        self.phone_number = phone_number



class PhoneBook():

    def __init__(self):
        self.contacts = []


    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact: Contact):

        for i in range(len(self.contacts)):
            if contact.name==self.contacts[i].name:
                print("The contact is already present in the list")
                return 
        
        if check(contact.phone_number):
            self.contacts.append(contact)

        # print(self.contacts)

    def remove_contact(self,name):                         

        for i in range(len(self.contacts)):

            if name==self.contacts[i].name:
                print(f"The contact Name: {name} and Phone Number: {self.contacts[i].phone_number} is removed\n")
                del self.contacts[i]
                return 
        print("contact not found!")

    def search_name(self,name):

        for i in range(len(self.contacts)):
            # print(i)

            if name==self.contacts[i].name:
                
                return self.contacts[i]
                
        return None

    
    def search_phone_number(self,phone_number):

        for i in range(len(self.contacts)):

            if phone_number==self.contacts[i].phone_number:

                return self.contacts[i]
                
        return None
    
    def display_by_gen(self):
        gen=( (key,value) for (key,value) in self.contacts.items())
        
        for i in gen:
            print(i)

    