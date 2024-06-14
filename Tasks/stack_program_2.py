

class Stack:


    def __init__(self,max_len=10):
        self.stack=[]
        self.max_len=max_len
    

    def push(self,url:str):

        if self.stack_size==self.max_len:
            print("The stack is Overflow")
            return 
        self.stack.append(url)

    def pop(self)-> str:

        if self.stack_size==0:
            print("The Stack is underflow")
            return 
        
        print("The element poped is :",self.stack.pop())

    def peek(self):
        
        if self.stack_size<0:
            print("The stack is underflow")

        print(f"The peek element is : {self.stack[self.stack_size-1]}")
    


    @property
    def stack_size(self):

        return len(self.stack)

    # def __len__(self):

    def search(self,url):
        new_stack=[]
        flag=0
        for i in range(self.stack_size):
            ele=self.stack.pop()
            new_stack.append(ele)
            if ele==url:
                flag=1
            
        self.stack.extend(new_stack[::-1])

        if flag==0:
            print("The element is Not in the stack")
        else:
            print("The url is present in the stack ")
                
    def __lt__(self,value):
        return len(self.stack)<value
    
    def __gt__(self,value):
        return self.size>value
    
    def __eq__(self, value):

        return self.size==value
    
    def __ne__(self, value):
        return self.size!=value
    
     

    @property
    def size(self):
        return len(self.stack)


if __name__=="__main__":
    s=Stack()

    s.push("1")
    s.push("2")
    s.push("3")
    s.push("4")
    s.push("5")
    s.push("6")

    s.peek()

    s.pop()
    s.peek()

    s.search("3")

    print()

    print("The size of the stack is : ",s.size)
    print("<",s<2)
    print(">",s>2)
    print("==",s==2)
    print("!=",s!=2)



