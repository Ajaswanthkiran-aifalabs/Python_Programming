


import json

from validators import check


class Commands():

    def __init__(self):

        with open("phonebook.json") as f:

            data=json.load(f)
        self.contacts=data

    def insert(self,name,ph):

        if name in self.contacts:
            print("Contact already present")
            return 
        if check(ph):
            print("frvtbgrte")
            self.contacts[name]=ph
        # print(self.contacts)

    def delete(self,name):
        
        if name in self.contacts:
            print("The contact Name: {name} and Phone Number: {self.contacts.}")
            del self.contacts[name]
            return 
        print("contact not found!")
    

    def search(self,name):
        
        if name in self.contacts:
            print(f"Contact found the Name: {name} and phone number {self.contacts[name]}")
            return
        print("contact not found!")

    def display(self):    

        if len(self.contacts)==0:

            print("Contains zero contacts")
        # print(self.contacts)
        for key,value in self.contacts.items():

            print(f"Name: {key} and phone number: {value}")

    def exit(self):

        with open("phonebook.json","w")  as f:
            json.dump(self.contacts,f)  
        
    def display_by_gen(self):
        det=( (key,value) for (key,value) in self.contacts.items())
        print(next(det))

    def list_comp(self):
        pass

    def itertools_func(self):
        pass