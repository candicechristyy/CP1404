"""
CP1404/CP5632 Practical
Program to generate lines of random numbers
"""
import random
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45
VALUES_PER_LINE = 6
amount_of_picks = int(input("How many quick picks? "))
for i in range(amount_of_picks):
    values = []
    while len(values) < VALUES_PER_LINE:
        random_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        if random_number not in values:
            values.append(random_number)
    values.sort()
    print(" ".join(f"{value:2}" for value in values))