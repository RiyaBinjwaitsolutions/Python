class Vehicle:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):

    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats

    def display_info(self):
        print(f"Car Detail:\nbrand: {self.brand}, model: {self.model}, seats: {self.seats}")

class Bike(Vehicle):

    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

    def display_info(self):
        print(f"Bike Detail:\nBrand:{self.brand}, Model:{self.model}, engine_cc:{self.engine_cc}")


c1=Car("tata","safari",7)
c1.display_info()

B1=Bike("Yamaha", "R15", 155)
B1.display_info()