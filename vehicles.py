class Vehicle:
    def __init__(self,  max_speed, brand, model):
        self.max_speed =  max_speed
        self.brand = brand
        self.model = model
    
    def drive(self):
        print (f'the max speed of {self.brand}{self.model} is {self.max_speed}')

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass




