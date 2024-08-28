class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

my_bus = Bus(100, 15000)
print(my_bus.max_speed)
print(my_bus.mileage)
print(my_bus)
