
# inheritance_lab.py

# Parent Class
class Vehicle:
    def __init__(self, brand, **kwargs):
        self.brand = brand
        print(f"Vehicle constructor called for {self.brand}")

    def info(self):
        print(f"Brand: {self.brand}")


# Child Class 1
class Car(Vehicle):
    def __init__(self, doors, **kwargs):
        super().__init__(**kwargs)
        self.doors = doors
        print(f"Car constructor called with {self.doors} doors")

    def info(self):
        super().info()
        print("This vehicle is a Car")


# Child Class 2
class Electric(Vehicle):
    def __init__(self, battery, **kwargs):
        super().__init__(**kwargs)
        self.battery = battery
        print(f"Electric constructor called with {self.battery} kWh battery")

    def info(self):
        super().info()
        print("This vehicle is Electric")


# Multiple Inheritance (Diamond Problem)
class ElectricCar(Car, Electric):
    def __init__(self, brand, doors, battery):
        super().__init__(
            brand=brand,
            doors=doors,
            battery=battery
        )
        print("ElectricCar constructor called")

    def info(self):
        super().info()
        print(f"Battery Capacity: {self.battery} kWh")
        print(f"{self.brand} is an Electric Car")


# Main Program
ecar = ElectricCar(
    brand="Tesla",
    doors=4,
    battery=75
)

print("\n=== Vehicle Information ===")
ecar.info()

print("\n=== Method Resolution Order (MRO) ===")
print(ElectricCar.__mro__)
