

class Product:
    
    def __init__(self,title,price):
        self.title = title
        self.price = price
    
    def apply_discount(self,per):
        self.price = self.price - (self.price * per/100)

    
class Ebook(Product):

    def __init__(self, title, price,pages):
        super().__init__(title,price)
        self.pages = pages


# book=Ebook("AJK",100,3432)

# print(book.price)

# book.apply_discount(10)

# print(book.price)


class Cart:


    def __init__(self) :

        self.products=[]

    def addProduct(self,product):
        self.products.append(product)

    def totalPrice(self):
        total=0
        for i in self.products:

            total+=i.price
        return total
    
c=Cart()

c.addProduct(Ebook("AJK",100,3432))

c.addProduct(Product("Ice Cream",44))

c.addProduct(Product("Drink",40))

c.addProduct(Ebook("I am legend",232,233))


print("The Total Price of the Cart: ",c.totalPrice())



        