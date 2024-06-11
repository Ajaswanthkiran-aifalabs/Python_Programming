from collections import deque

class TreeNode:

    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

    
class BinaryTree:

    def __init__(self):
        self.root=None

    def insert(self,val):


        if self.root is None:
            self.root=TreeNode(val)
        
        d=deque()
        d.append(self.root)

        while d:
            node=d.popleft()

            if node.left is None:
                node.left=TreeNode(val=val)
                break
            else:
                d.append(node.left)
            
            if node.right is None:
                node.left=TreeNode(val)
                break
            else:
                d.append(node.right)

        return self.root
    
    def preorder(self):

        self.display_preorder(self.root)
    
    def display_preorder(self,node):

        if node is None:
            return 
        else:
            self.display_preorder(node.left)
            print(node.val,"-> ",end=" ")
            self.display_preorder(node.right)



def main():

    t=BinaryTree()

    t.insert(1)
    t.insert(2)

    t.preorder()

if __name__=="__main__":
    main()