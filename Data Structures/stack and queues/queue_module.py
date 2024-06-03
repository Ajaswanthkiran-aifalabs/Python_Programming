from queue import LifoQueue

def main():

    stack=LifoQueue(maxsize=10)

    stack.put(10)
    stack.put_nowait(20)
    stack.put(3)

    print(stack.empty())

    print(stack.get())

    print(stack.full())
 

if __name__=="__main__":
    main()