

from linked_list_node import Node

import random

class LinkedList:


    def __init__(self):
        self.customers={}
        self.head=None

    # @property
    # def status(self):
    #     return self.status
    
    # @status.setter
    # def status(self):

    #     self.status=random.choice(['CNF','WL'])


        
    def insert(self,name,id):
        status=random.choice(['CNF','WL'])
        pr=random.choice([True,False])
        newnode=Node(name,id,status,pr)

        if name in self.customers:
            print("The user already booked a ticket")
            return 
        

        self.customers[name]=newnode
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next

            temp.next=newnode
        
    def delete_by_name(self,name):
        temp=self.head

        if self.head==None:
            print("No customers")
            return 
        if temp.name==name:
            self.head=temp.next
            return 
        flag=0
        while temp.next.next:
            if temp.next.name==name:
                flag=1
                break
            temp=temp.next

        if flag==0:
            print("The element is not found")
            return 
        print(temp.name)

        temp.next=temp.next.next

    
    def delete_by_id(self,id):
        
        temp=self.head

        if self.head==None:
            print("No customers")
            return 
        if temp.id==id:
            self.head=temp.next
            return 
        flag=0
        while temp.next.next:
            if temp.next.id==id:
                flag=1
                break
            temp=temp.next

        if flag==0:
            print("The element is not found")
            return 
        print(temp.name)

        temp.next=temp.next.next
    

    def display(self):

        temp=self.head
        print()
        while temp:
            print(f"Name: {temp.name}  Id: {temp.id} Status: {temp.status} Priority: {temp.priority}")
            temp=temp.next
        print()

    def get_higher_priority(self):

        temp=self.head
        print()
        while temp:
            if temp.priority:
                print(f"Name: {temp.name}  Id: {temp.id} Status: {temp.status} Priority: {temp.priority}")
            temp=temp.next
        print()

if __name__=="__main__":

    ll=LinkedList()
    ll.insert("a",1)
    ll.insert("b",2)
    ll.insert("c",3)
    ll.insert("d",4)
    ll.insert("e",5)
    ll.insert("f",6)
    ll.display()

    ll.delete_by_id(4)

    ll.display()

    ll.delete_by_name("b")

    ll.display()

    
    ll.insert("f",6)


    ll.get_higher_priority()