import random
"""
CP1404/CP5632 - Practical
Program to determine score status, generate random score and print result
"""
def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        print(determine_result(score))
    score = random.randint(0, 100)
    print(f"Random score: {score}\n{determine_result(score)}")


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()