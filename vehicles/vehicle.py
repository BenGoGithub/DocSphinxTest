from .abstract_vehicle import AbstractVehicle


class Vehicle(AbstractVehicle):
    """Concrete class implementing AbstractVehicle."""

    def display_info(self):
        return f"{self.year} {self.make} {self.model} - Mileage: {self.mileage} km, Fuel Consumption: {self.fuel_consumption} L/100km"

    def calculate_fuel_efficiency(self):
        pass

    def update_mileage(self, param):
        pass
