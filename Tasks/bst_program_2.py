from tree_structure import Tree


from collections import deque


class LevelOrder:

    def __init__(self,node,level):
        self.temp=node
        self.level=level

class BST:


    def __init__(self):
        self.root=None
    

    def insert(self,name,ph):
        self.root=self.insert_node(self.root,name,ph)
    def insert_node(self,root,name,ph):
        
        if root is None:
            return Tree(name,ph)
        else:
            if name==root.name:
                return root
            elif name>root.name:
                root.left=self.insert_node(root.left,name,ph)
            else:
                root.right=self.insert_node(root.right,name,ph)
        return root
    
    def display_inorder(self):

        self.inorder(self.root)
    
    def inorder(self,root):

        if root!=None:
            self.inorder(root.left)
            print(root.name)
            self.inorder(root.right)

    def level_order(self):
        queue=deque()

        queue.append(LevelOrder(self.root,0))
        dict={}
        while queue:
            ele=queue.popleft()

            temp=ele.temp
            level=ele.level
            if temp.right is not None:
                queue.append(LevelOrder(temp.right,level+1))
            
            if temp.left is not None:
                queue.append(LevelOrder(temp.left,level+1))
            
            if level in dict:
                dict[level].append(temp.name)
            else:
                dict[level]=[temp.name]
            
        print(dict)


    def deleteNode(self,name):

        self.delete(self.root,name)

    def delete(self,root,name):

        if root is None:
            return root
        
        if root.name>name:
            root.left=self.delete(root.left,name)
        elif root.name<name:
            root.right=self.delete(root.right,name)

        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp=self.minvalue(root.right)
            root.name=temp.name
            root.phno=temp.phno

            print(root.name)
            root.right= self.delete(root.right,temp)
        
        return root

    def minvalue(self,root):
        node=root
        while node!=None and node.left!=None :
            node=node.left
           
        return node
    
    def search(self,name):

        temp=self.search_helper(self.root,name)

        if temp is None:
            print("Not Found!")
        else:
            print(f"The phone number of the user {name} is {temp.phno}")
    def search_helper(self,root,name):
        
        if root==None or root.name==name:
            
            return root
        
        elif root.name<name:
            return self.search_helper(root.right,name)
       
        return self.search_helper(root.left,name)

if __name__=="__main__":
    bst=BST()
    bst.insert("c",3)
    bst.insert("a",1)
    bst.insert("b",2)
    bst.insert("E",1)
    bst.insert("F",2)
    bst.display_inorder()

    bst.level_order()
    bst.search("E")

    print("-------------------")
    bst.deleteNode("E")
    print("------------------------")
    bst.display_inorder()

    bst.level_order()

    

