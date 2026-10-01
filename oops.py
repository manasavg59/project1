# VEHICLE RENTAL MANAGEMENT SYSTEM

from abc import ABC, abstractmethod


# ---------- PARENT CLASS ----------

class Vehicle(ABC):

    def __init__(self, vehicle_number, brand):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.is_available = True

    def show_details(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Available:", self.is_available)

    @abstractmethod
    def calculate_rent(self, days):
        pass


# ---------- CAR CLASS ----------

class Car(Vehicle):

    def __init__(self, vehicle_number, brand):
        super().__init__(vehicle_number, brand)
        self.rent_per_day = 1500
    
    def calculate_rent(self, days):
        return self.rent_per_day * days


# ---------- BIKE CLASS ----------

class Bike(Vehicle):

    def __init__(self, vehicle_number, brand):
        super().__init__(vehicle_number, brand)
        self.rent_per_day = 500

    def calculate_rent(self, days):
        return self.rent_per_day * days


# ---------- TRUCK CLASS ----------

class Truck(Vehicle):

    def __init__(self, vehicle_number, brand):
        super().__init__(vehicle_number, brand)
        self.rent_per_day = 2500

    def calculate_rent(self, days):
        return self.rent_per_day * days


# ---------- CUSTOMER CLASS ----------

class Customer:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# ---------- RENTAL CLASS ----------

class Rental:

    def __init__(self, customer, vehicle, days):

        self.customer = customer
        self.vehicle = vehicle
        self.days = days

        self.total_rent = vehicle.calculate_rent(days)

    def show_rental_details(self):

        print("\n========== RENTAL DETAILS ==========")

        print("Customer Name :", self.customer.name)
        print("Phone         :", self.customer.phone)
        print("Vehicle       :", self.vehicle.brand)
        print("Vehicle Number:", self.vehicle.vehicle_number)
        print("Rental Days   :", self.days)
        print("Total Rent    :", self.total_rent)


# ---------- CREATE VEHICLE OBJECTS ----------

car = Car("KA01AB1234", "Toyota")
bike = Bike("KA02CD5678", "Honda")
truck = Truck("KA03EF9012", "Tata")


# ---------- CUSTOMER DETAILS ----------

print("========================================")
print("      VEHICLE RENTAL MANAGEMENT")
print("========================================")

name = input("\nEnter customer name: ")
phone = input("Enter phone number: ")

customer = Customer(name, phone)


# ---------- MAIN MENU ----------

while True:

    print("\n================================")
    print("             MENU")
    print("================================")

    print("1. View Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = input("\nEnter choice: ")


    # ---------- VIEW VEHICLES ----------

    if choice == "1":

        print("\n========== AVAILABLE VEHICLES ==========")

        print("\n1. Car")
        car.show_details()
        print("Rent per day: ₹", car.rent_per_day)

        print("\n2. Bike")
        bike.show_details()
        print("Rent per day: ₹", bike.rent_per_day)

        print("\n3. Truck")
        truck.show_details()
        print("Rent per day: ₹", truck.rent_per_day)


    # ---------- RENT VEHICLE ----------

    elif choice == "2":

        print("\n========== RENT VEHICLE ==========")

        print("1. Car")
        print("2. Bike")
        print("3. Truck")

        vehicle_choice = input("\nEnter vehicle choice: ")


        if vehicle_choice == "1":

            selected_vehicle = car

        elif vehicle_choice == "2":

            selected_vehicle = bike

        elif vehicle_choice == "3":

            selected_vehicle = truck

        else:

            print("\nInvalid vehicle choice.")
            continue


        # Check vehicle availability

        if selected_vehicle.is_available:

            days = int(input("Enter number of rental days: "))

            rental = Rental(customer, selected_vehicle, days)

            selected_vehicle.is_available = False

            print("\nVehicle rented successfully!")

            rental.show_rental_details()

        else:

            print("\nVehicle is not available.")


    # ---------- RETURN VEHICLE ----------

    elif choice == "3":

        print("\n========== RETURN VEHICLE ==========")

        print("1. Car")
        print("2. Bike")
        print("3. Truck")

        vehicle_choice = input("\nEnter vehicle choice: ")


        if vehicle_choice == "1":

            if car.is_available:
                print("\nCar is already available.")

            else:
                car.is_available = True
                print("\nCar returned successfully.")


        elif vehicle_choice == "2":

            if bike.is_available:
                print("\nBike is already available.")

            else:
                bike.is_available = True
                print("\nBike returned successfully.")


        elif vehicle_choice == "3":

            if truck.is_available:
                print("\nTruck is already available.")

            else:
                truck.is_available = True
                print("\nTruck returned successfully.")


        else:

            print("\nInvalid vehicle choice.")


    # ---------- EXIT ----------

    elif choice == "4":

        print("\nThank you for using Vehicle Rental Management System.")
        break


    # ---------- INVALID MENU CHOICE ----------

    else:

        print("\nInvalid choice. Please try again.")