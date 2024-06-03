

from collections import deque



def main():
    stack=deque()

    stack.append(10)
    stack.append(23)
    stack.append(54)
    print(stack)
    print(stack.pop())
    print("-->",len(stack))
    print(stack.pop())
    print(stack.pop())
    print(stack)

    if not stack:
        print(stack)
if __name__=="__main__":
    main()