


class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def apply_discount(self,percentage):

        self.price = self.price-(self.price*percentage)

    
class Ebook(Product):

    def __init__(self,name,price,pages):
        super().__init__(name,price)
        self.pages = pages
    

class Cart:

    def __init__(self):
        self.products=[]


    def addProduct(self,product):
        self.products.append(product)

    def sortByPrice(self):
        self.products.sort(key = lambda products: products.price)

    def display_all_products(self):
        total=0
        for i in self.products:
            print(f"{i.name:<12}{i.price:>12}")
            total+=i.price
        
        print(f"{total=}")
    
    


    

c=Cart()

c.addProduct(Product("Milk",30))
c.addProduct(Product("Apple",50))
c.addProduct(Product("Candy",23))
c.addProduct(Ebook("AJK",2342,2134342))
c.addProduct(Product("5star",10))

c.display_all_products()

c.sortByPrice()

print("After the sort")

c.display_all_products()