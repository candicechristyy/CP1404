"""
CP1404/CP5632 Practical
Client program to test Taxi class
"""
from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(my_taxi, f"\nCurrent fare: ${my_taxi.get_fare():.2f}")
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, f"\nCurrent fare: ${my_taxi.get_fare():.2f}")