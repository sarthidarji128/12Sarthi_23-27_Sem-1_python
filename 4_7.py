class Grandfather:
    def __init__(self, house, car):
        self.house = house
        self.car = car

class Father(Grandfather):
    def __init__(self, house, car, land):
        super().__init__(house, car)
        self.land = land

class Child(Father):
    def __init__(self, house, car, land, savings):
        super().__init__(house, car, land)
        self.savings = savings
child = Child("mansion", "luxury car & bike & tracktor", "farm & 49 bhega Land", 100000)

# Access inherited assets
print(f"House: {child.house}")
print(f"Car: {child.car}")
print(f"Land: {child.land}")
print(f"Savings: {child.savings}","₹")
