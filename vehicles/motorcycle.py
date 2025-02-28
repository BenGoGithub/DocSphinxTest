from .vehicle import Vehicle

class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""

    def __init__(self, make, model, year, mileage, fuel_consumption, engine_capacity: float):
        super().__init__(make, model, year, mileage, fuel_consumption)
        self.engine_capacity = engine_capacity  # Specific attribute for motorcycles

    def display_info(self):
        return f"{self.year} {self.make} {self.model} - Mileage: {self.mileage} km, Fuel Consumption: {self.fuel_consumption} L/100km, Engine Capacity: {self.engine_capacity} cc"

    def calculate_fuel_efficiency(self):

        return 100 / self.fuel_consumption  # km/L

    def honk(self):
        """Honk the motorcycle horn. """
        return "Peep peep! 🏍️"