

class Vehicle:

    def __init__(self,brand,model,price):
        self.brand = brand  
        self.model = model  
        self.price=price
    
    def show(self):
        print("Details: ",self.brand,self.model,self.price)
    
    def max_speed(self):
        print("Max Speed: 200 km/h")
    
    def gear(self):
        print("Gear: 5")
    
class Car(Vehicle):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
    
    def show(self):
        print("The Car Details are: ",self.brand,self.model,self.price)

    def max_speed(self):
        print("max speed is 450")
    
    def gear(self):
        print("Auto")
    

car=Car("BMW",3,34314)
car.show()
car.max_speed()
car.gear()
print("")
vehicle=Vehicle("Tata",2,4532)

vehicle.show()

vehicle.max_speed()

vehicle.gear()


