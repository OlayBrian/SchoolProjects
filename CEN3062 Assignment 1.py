from abc import ABC, abstractmethod

# Single Responsibility
class Driver:
    def __init__(self, name):
        self.name = name
        self.available = True

class Customer:
    def __init__(self, name):
        self.name = name

# Open/Closed Principle 
class RideType(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class EconomyRide(RideType):
    def calculate_fare(self, distance):
        return distance * 5

class LuxuryRide(RideType):
    def calculate_fare(self, distance):
        return distance * 10

class PoolRide(RideType):
    def calculate_fare(self, distance):
        return distance * 3

# Dependency Inversion
class DriverManager:
    def __init__(self, drivers):
        self.drivers = drivers

    def get_available_driver(self):
        for driver in self.drivers:
            if driver.available:
                driver.available = False
                return driver
        return None 


class SwiftRide:
    def __init__(self, customer, start, end, distance, ride_type, driver_manager):
        self.customer = customer
        self.start = start
        self.end = end
        self.distance = distance
        self.ride_type = ride_type
        self.driver = driver_manager.get_available_driver()

    def get_ride(self):
        if self.driver:
            fare = self.ride_type.calculate_fare(self.distance)
            print(f"Total price: ${fare}, Driver: {self.driver.name}")
        else:
            print("ERROR! NO DRIVERS AVAILABLE!")


drivers = [Driver("Alice"), Driver("Bob")]
driver_manager = DriverManager(drivers)


john = Customer("John")
rebecca = Customer("Rebecca")
mike = Customer("Mike")


ride1 = SwiftRide(john, "Airport", "Downtown", 15, EconomyRide(), driver_manager)
ride1.get_ride()

ride2 = SwiftRide(rebecca, "College", "Downtown", 10, LuxuryRide(), driver_manager)
ride2.get_ride()

ride3 = SwiftRide(mike, "Downtown", "Shopping Mall", 5, PoolRide(), driver_manager)
ride3.get_ride() 
