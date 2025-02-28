from abc import ABC, abstractmethod


class AbstractVehicle(ABC):
    """Abstract class defining a vehicle."""

    def __init__(self, make: str, model: str, year: int, mileage: float, fuel_consumption: float):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def display_info(self):
        """Abstract method to display vehicle information."""
        pass
