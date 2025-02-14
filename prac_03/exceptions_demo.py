"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when the user enters a non-integer input like letters and symbols.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters 0 for the denominator as numbers divided by 0 is mathematically undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I can change the code to avoid getting ZeroDivisionError by using a while loop to check to user input.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
