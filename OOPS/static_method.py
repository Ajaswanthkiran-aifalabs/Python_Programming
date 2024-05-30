

class Product:


    @staticmethod
    def fun():
        print("This is a static method")


    @classmethod
    def func(cls):
        print("This is a class method: ",cls)

p=Product()

p.fun()
p.func()