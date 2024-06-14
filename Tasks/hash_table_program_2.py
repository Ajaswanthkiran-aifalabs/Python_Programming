


class HashTable:


    def __init__(self):
        self.dict={}

    def register(self,name,password):

        if name  in self.dict:
            print("The user is already present change the name")
            return 
        print("The user {name} is registered")
        self.dict[name]=password

    def login(self,name,password):

        if name not in self.dict:
            raise Exception(f"\nThere is no user present with the name {name}")
             
    
        if password is not self.dict[name]:
            raise  Exception("\nPassword is Incorrect")
             
        print("\nThe provided user name and password is correct")
    
    def delete(self,name):

        if name not in self.dict:
            print("The user name is not present")

        print(f"The credentials of '{name}' is deleted")
        del self.dict[name]

    def display(self):

        print()
        print("The list of credentials are: ")
        for key,value in self.dict.items():
            print(f"Name: {key}  Password: {value}")

        print()

    def search(self,name):
        if name not in self.dict:
            print("The credentials are not found")
            return

        print(f"The credentials are found Name: {name}  password: {self.dict[name]}")

if __name__=="__main__":

    
    try:
        ht=HashTable()

        ht.register("a","aa")
        ht.register("asd","wqec")


        ht.display()



        ht.delete("a")



        ht.display()

        ht.search("asd")

        ht.login("asd","wqe")
    except Exception as e:
        print(e)


