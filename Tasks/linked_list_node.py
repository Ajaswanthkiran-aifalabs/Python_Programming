

class Node:

    def __init__(self,name,id,s,p):
        self.name=name
        self.id=id
        self.status=s
        self.priority=p
        self.next=None