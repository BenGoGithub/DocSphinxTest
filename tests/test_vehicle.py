import pytest
from vehicles.vehicle import Vehicle


def test_vehicle_creation():
    """Test creation of a Vehicle instance."""
    car = Vehicle(make="Toyota", model="Corolla", year=2020, mileage=15000, fuel_consumption=6.5)

    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020
    assert car.mileage == 15000
    assert car.fuel_consumption == 6.5


def test_update_mileage():
    """Test mileage update."""
    car = Vehicle(make="Toyota", model="Corolla", year=2020, mileage=15000, fuel_consumption=6.5)
    car.update_mileage(200)

    assert car.mileage == 15200


def test_fuel_efficiency():
    """Test fuel efficiency calculation."""
    car = Vehicle(make="Toyota", model="Corolla", year=2020, mileage=15000, fuel_consumption=6.5)

    efficiency = car.calculate_fuel_efficiency()
    assert efficiency == pytest.approx(15.384, rel=1e-3)  # Vérifie avec une tolérance

import pytest
from vehicles.car import Car
from vehicles.truck import Truck
from vehicles.motorcycle import Motorcycle

# Test Car
def test_car():
    car = Car(make="Toyota", model="Corolla", year=2020, mileage=15000, fuel_consumption=6.5, doors=4)
    assert car.display_info() == "2020 Toyota Corolla - Mileage: 15000 km, Fuel Consumption: 6.5 L/100km"
    assert car.honk() == "Beep beep! 🚗"

# Test Truck
def test_truck():
    truck = Truck(make="Volvo", model="FH", year=2022, mileage=50000, fuel_consumption=30.0, load_capacity=20)
    assert truck.display_info() == "2022 Volvo FH - Mileage: 50000 km, Fuel Consumption: 30.0 L/100km, Load Capacity: 20 tons"
    assert truck.honk() == "HOOOOOONK! 🚚"

# Test Motorcycle
def test_motorcycle():
    motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2021, mileage=1200, fuel_consumption=5.0, engine_capacity=1200)
    assert motorcycle.display_info() == "2021 Harley-Davidson Sportster - Mileage: 1200 km, Fuel Consumption: 5.0 L/100km, Engine Capacity: 1200 cc"
    assert motorcycle.honk() == "Peep peep! 🏍️"
