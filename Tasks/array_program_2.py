


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    

class Inventory:

    def __init__(self):
        self.products=[]
    
    def delete_by_name(self,name):

        for i in self.products:
            if i.name==name:
                self.products.remove(i)
                return 

    def delete_by_price(self,price):
        for i in self.products:
            if i.price==price:
                self.products.remove(i)
                return 
        
    def display(self):
        print()
        for i in self.products:
            print(f"Name: {i.name} price: {i.price}")
        print()
    def search_price_by_name(self,name):
        
        for i in self.products:
            if i.name==name:
                print(f"The Price of the Product {name} is {i.price}")
                return True
        return False
    

    @property
    def get_size(self):
        return len(self.products)

    def search_products_n_by_3(self,count):
        dict={}
        n=self.get_size
        n-=1
        while True:

            if n<0:
                break

            i=self.products[n]
            if i.price in dict:
                dict[i.price].append(i.price)
            else:
                dict[i.price]=[i.price]
            
            n-=1
        print("The products with the same price existing more than {n}/3 time")
        # print(dict.items())
        dict={key: value for key,value in dict.items()  if len(value)>=count}
        
        for key,values in dict.items():
            print(f"Price:{key} Products: {values}")

    def filter_by_price(self,price):

        lst=[i for i in self.products if i.price>=price]

        for i in lst:
            print(f"Name: {i.name} Price: {i.price}")
        
if __name__=="__main__":
    inv=Inventory()

    inv.products.append(Product("A",1))
    inv.products.append(Product("B",2))
    inv.products.append(Product("C",3))
    inv.products.append(Product("D",4))
    inv.products.append(Product("E",4))
    inv.products.append(Product("F",4))
    
    inv.products.append(Product("G",2))
    inv.products.append(Product("H",3))
    inv.products.append(Product("I",9))
    inv.products.append(Product("J",5))
    inv.products.append(Product("K",7))
    inv.products.append(Product("L",2))
    
    inv.display()

    inv.delete_by_price(3)

    inv.display()
 
    if not inv.search_price_by_name("A"):
        print("Product not found")
    print()
    inv.search_products_n_by_3(inv.get_size//3)
    inv.filter_by_price(4)