class Combustible(Car):
    def __init__(self, name, km):
        self.super(name, "Combustible", km)
        self.number_of_km = 100
        self.remaining_km += km

    def refill(self, km):
        print("fully refilled with gas ")

class E_Car(Car):
    def __init__(self, name, Electro, km ) 
        self.super(name, "Electro", km)
        self.batteryload = 100

    def refill(self, km):
        print("fully refilled with green electricity")
