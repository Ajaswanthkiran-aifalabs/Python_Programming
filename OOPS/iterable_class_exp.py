


from dataclasses import dataclass
@dataclass
class Product:

    name: str
    price: int


class Cart:

    def __init__(self):

        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def total_products(self):
        return len(self.products)
    
    def __iter__(self):
        self.count=0
        return self
    
    def __next__(self):
        if self.count<self.total_products():
            ele=self.products[self.count]
            self.count+=1
            return ele
        elif self.count>=self.total_products() :
            raise StopIteration
        

c=Cart()

c.add_product(Product("Milk",250))
c.add_product(Product("Ice Cream",450))

for i in c:
     print(i.name,i.price)