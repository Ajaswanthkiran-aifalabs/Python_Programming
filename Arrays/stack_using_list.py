
class Stack:

    def __init__(self,):

        self.stack=[]
        self.max_size=10

    def push(self,value):

        if  len(self.stack)==self.max_size:
            print("Stack is OverFlow")
        else:
            self.stack.append(value)
        
    def pop(self):

        if len(self.stack)==0:
            print("Stack is Under Flow")
        else:
            print(f"Removed element: {self.stack.pop()}")

    def peek(self):
        if len(self.stack)==0:
            print("Stack is under flow")
        else:
            print(f"Peek: {self.stack[len(self.stack)-1]}")
        
   
def main():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.peek()
    stack.pop()
    stack.pop()
    stack.pop()


if __name__=="__main__":
    main()