from .vehicle import Vehicle

class Truck(Vehicle):
    """Truck class inheriting from Vehicle."""

    def __init__(self, make, model, year, mileage, fuel_consumption, load_capacity: float):
        super().__init__(make, model, year, mileage, fuel_consumption)
        self.load_capacity = load_capacity  # Specific attribute for trucks

    def display_info(self):
        return f"{self.year} {self.make} {self.model} - Mileage: {self.mileage} km, Fuel Consumption: {self.fuel_consumption} L/100km, Load Capacity: {self.load_capacity} tons"

    def calculate_fuel_efficiency(self):
        return 100 / self.fuel_consumption  # km/L

    def honk(self):
        """Honk the truck horn. """
        return "HOOOOOONK! 🚚"
