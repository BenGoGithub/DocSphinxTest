import numpy as np
from vehicles.car import Car
from vehicles.truck import Truck
from vehicles.motorcycle import Motorcycle


def main():
    # Creation of vehicle instances
    car = Car(make="Toyota", model="Corolla", year=2020, mileage=15000, fuel_consumption=6.5, doors=4)
    truck = Truck(make="Volvo", model="FH", year=2022, mileage=50000, fuel_consumption=15.0, load_capacity=20)
    motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2021, mileage=1200, fuel_consumption=2.2,
                            engine_capacity=1200)

    # Display information about the vehicles
    print(car.display_info())
    print(truck.display_info())
    print(motorcycle.display_info())

    # Decimals rounded to the nearest tenth
    car_efficiency = np.ceil(car.calculate_fuel_efficiency() * 10) / 10
    truck_efficiency = np.ceil(truck.calculate_fuel_efficiency() * 10) / 10
    motorcycle_efficiency = np.ceil(motorcycle.calculate_fuel_efficiency() * 10) / 10

    # Update mileage
    print(f"Fuel Efficiency (Car): {car_efficiency} km/l")
    print(f"Fuel Efficiency (Truck): {truck_efficiency} km/l")
    print(f"Fuel Efficiency (Motorcycle): {motorcycle_efficiency} km/l")

    # Honk the horn
    print(car.honk())
    print(truck.honk())
    print(motorcycle.honk())


if __name__ == "__main__":
    main()
