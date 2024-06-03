

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
    


class LinkedList:


    def __init__(self):
        self.head=None

    def insert_at_End(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head=new_node
            return 
        else:
            current_node=self.head

            while current_node.next:
                current_node=current_node.next
            
            current_node.next=new_node
    def reverse(self):
        curr=self.head
        prev=next=None

        if curr is None:
            return None
        
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev


    def insert_at_beginning(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next = self.head
            self.head =new_node

    def insert_at_any_position(self,pos,value):

        new_node=Node(value)

        if self.head is None:
            self.head = new_node
            return
        elif pos==0:
            self.insert_at_beginning(value)
            return
        else:
            curr_node=self.head

            count=1
            while (curr_node!=None and (count+1)!=pos) :
                curr_node=curr_node.next
                count+=1
                
            if curr_node!=None:
                new_node.next=curr_node.next
                curr_node.next=new_node
            else:
                print("Index not found")
                 
    def display(self):

        if self.head is None:
            print("Linked list is empty")
            return 

        curr_node=self.head

        while curr_node:
            print(f"{curr_node.data} ",end="-> ")
            curr_node=curr_node.next
        print()

    def updateNode(self,pos,value):

        if pos==1:
            self.head.data = value
        else:
            curr_node = self.head

            position=1
            while (curr_node!=None and position+1!=pos):
                curr_node = curr_node.next
                position+=1

            if curr_node!=None:
                curr_node.data=value
            else:
                print("Index not found")

    def deleteAtBegin(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            self.head=self.head.next
    def deleteAtEnd(self):

        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head=None
        else:
            curr_node = self.head

            while curr_node.next.next!=None:
                curr_node=curr_node.next
            print(curr_node.data)
            curr_node.next=None
        
    def deleteAtAny(self,pos):

        if self.head is None:
            print("Linked List is empty")
        else:
            curr_node = self.head

            position=1

            while (curr_node!=None and (position+1)!=pos):
                curr_node=curr_node.next
                position+=1

            # print(curr_node.data)
            curr_node.next=curr_node.next.next
        
    def search(self,value):


        if self.head is None:
            print("Linked List is empty")
        else:
            
            curr_node=self.head
            pos=1
            while curr_node:
                if curr_node.data==value:
                    print("Element found at index: ",pos)
                    return 
                pos+=1
                curr_node=curr_node.next
            print("Element not found")

                

def main():


    l=LinkedList()
    l.insert_at_End(10)

    l.insert_at_End(89)

    l.insert_at_End(23)

    l.display() 

    l.insert_at_beginning(23) 

    l.display()

    l.insert_at_any_position(4,34)

    l.display()

    l.updateNode(4,543)

    l.display()


    l.deleteAtAny(5)

    l.display()

    # l.deleteAtBegin()

    # l.display()

    # l.deleteAtEnd()

    # l.display()
    # l.deleteAtEnd()

    # l.display()

    # l.deleteAtEnd()

    # l.display()

    l.search(543)


    l.reverse()

    l.display()


    


if __name__=="__main__":
    main()