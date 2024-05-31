
class Node:

    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None
class DoubleLinkedList:


    def __init__(self):
        self.head = None

    
    def insertAtBegin(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node.next
        
    def insertAtEnd(self,val):

        new_node=Node(val)

        if self.head is None:
            self.head = new_node
        else:
            crr=self.head

            while crr.next!=None:
                crr=crr.next
            
            crr.next=new_node
            new_node.prev=crr

    def insertAtIndex(self,value,pos):

        new_node=Node(value)
        if self.head is None:
            self.head=new_node

        else:
            crr=self.head
            position=1
            while (crr!=None and position+1!=pos):
                crr=crr.next
                position+=1

            if crr is None:
                print("Index not found")
                return
            
            if crr.next==None:
                self.insertAtEnd(value)

            new_node.next=crr.next
            new_node.prev=crr
            crr.next.prev=new_node
            crr.next=new_node

    def deleteAtStart(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            self.head=self.head.next
            self.head.prev = None

    def deleteAtEnd(self):

        if self.head is None:
            print("Linked is Empty")
        else:
            crr_node=self.head

            while crr_node.next!=None:

                crr_node=crr_node.next
            crr_node.prev.next=None
         
    
    def deleteAtIndex(self,pos):

        if self.head is None:
             print("Linked List is empty")
        else:
            crr_node=self.head
            position=1
            while (crr_node!=None and position+1!=pos):
                crr_node=crr_node.next
                position+=1
            if  crr_node is None:
                print("Index greater than the list")
                return 
            crr_node.next.prev=crr_node
            crr_node.next=crr_node.next.next

    def display_reverse(self):

        if self.head is None:
            print("Linked List is empty")
            return
        curr_node=self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
        
        while curr_node!=None:
            print(curr_node.data,end=" <- ")
            curr_node=curr_node.prev


            
    def display(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            crr=self.head
            while crr:
                print(crr.data,end=" -> ")
                crr=crr.next
        print()
    
def main():

    l=DoubleLinkedList()

    l.insertAtEnd(34)
    l.insertAtEnd(43)
    l.insertAtBegin(443)
    l.insertAtEnd(345343)

    l.display()

    l.insertAtEnd(342)
    l.insertAtBegin(3443)

    l.display()

    l.insertAtIndex(value=3,pos=3)
    l.display()

    l.insertAtIndex(7654,pos=5)
    l.display()

    l.insertAtIndex(98765,pos=7)
    l.display()

    l.deleteAtEnd()

    l.display()

    l.deleteAtStart()

    l.display()

    l.deleteAtIndex(6)

    l.display()

    l.display_reverse()


if __name__=="__main__":
    main()
