"""
Cohesion and coupling:
    High level concept. THey say how your code is easily changed or extended.
Cohesion: Degree to which elements of a certain class belong together. (Has a clear responsibility).
Coupling: is a measure of how dependent 2 parts of your code together. The more coupling the more difficult to maintain.
"""

# Code before improving the cohesion and coupling:
import string
import random


class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        # Low cohesion -> Many responsibilities.
        # High Coupling because it is relying on the VehicleRegistry class

        # Create registry instance
        registry = VehicleRegistry()

        # Generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # Generate license plate using the first characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # Compute the catalogue price
        catalogue_price = 0
        if brand == 'Tesla Model 3':
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # Generate the Tax (5% of the price, but for electric it is 2%
        tax_percentage = 0.05
        if brand == 'Tesla Model 3' or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # Payable tax
        payable_tax = tax_percentage * catalogue_price

        # Print info
        print("Registration complete")
        print(f"Brand: {brand}")
        print(f"ID: {vehicle_id}")
        print(f"License Plate: {license_plate}")
        print(f"Payable Tax: {payable_tax}")


# app = Application()
# app.register_vehicle("BMW 5")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Code after improving the cohesion and coupling:
# Find where the info is stored and how it is accessed.


class VehicleInfo:
    # Structure the data
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.compute_tax()}")


class Vehicle:
    # Structure the data
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"License Plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info ={}

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model S", True, 75000)

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        # Generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # Generate license plate using the first characters of the vehicle id
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    def register_vehicle(self, brand: string):
        # Create registry instance
        registry = VehicleRegistry()

        # Create a vehicle
        return registry.create_vehicle(brand)




app = Application()
vehicle = app.register_vehicle("Tesla Model 3")
# Print info
vehicle.print()