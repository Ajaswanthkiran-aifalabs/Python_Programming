


class Graph:

    def __init__(self):
        self.dict={}

    def insert(self,u,v):

        if u in self.dict:
            self.dict[u].append(v)
        else:
            self.dict[u]=[v]

        
        if v in self.dict:
            self.dict[v].append(u)
        else:
            self.dict[v]=[u]
    
    
    def delete(self,edge):

        del self.dict[edge]

        for key,value in self.dict.items():

            if edge in value:
                self.dict[key].remove(edge)
    
    def display(self):

        for key,value in self.dict.items():
            print(f"{key} : {value}")

    def display_connection(self,edge):

        if edge not in self.dict:
            print("The edge is not in the graph")
        
        print(f"The connection of {edge}: {self.dict[edge]}")

    def search(self,u,v):

        if u not in self.dict:
            print(f"There is no user with {u}")
            return 
        
        if v not in self.dict[u]:
            print(f"\nThere is no connection between {u}-->{v}")
            return 
        
        print(f"\nThere is a connection between {u}-->{v}")
        
        
if __name__=="__main__":
    g=Graph()

    g.insert("jaswanth","ravi")
    
    g.insert("kushal","ravi")
    
    g.insert("jaswanth","kushal")
    
    g.insert("jaswanth","krishna")
    
    g.insert("kushal","harsha")
    
    g.insert("krishna","ravi")

    g.insert("harsha","yaswanth")

    g.insert("AJK","jaswanth")

    
    g.insert("AJK","kushal")

    
    g.insert("AJK","ravi")    
    

    g.display()

    g.delete("AJK")

    print("\nAfter delete")

    g.display()

    g.search("jaswanth","yaswanth")

    g.search("jaswanth","kushal")
    print()
    g.display_connection("jaswanth")