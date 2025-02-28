from .vehicle import Vehicle

class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, make, model, year, mileage, fuel_consumption, doors: int):
        super().__init__(make, model, year, mileage, fuel_consumption)
        self.doors = doors  # Specific attribute for cars

    def display_info(self):
        return f"{self.year} {self.make} {self.model} - Mileage: {self.mileage} km, Fuel Consumption: {self.fuel_consumption} L/100km, Number of Doors: {self.doors}"

    def calculate_fuel_efficiency(self):
        return 100 / self.fuel_consumption  # km/L

    def honk(self):
        """Honk the car horn. """
        return "Beep beep! 🚗"

