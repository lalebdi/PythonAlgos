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
        # Create registry instance
        registry = VehicleRegistry()

        # Generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # Generate license plate using the first characters of the vehcile id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # Compute the catalogue price
        catalogue_price = 0
        if brand == 'Tesla Model 3':
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000