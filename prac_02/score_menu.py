"""
CP1404/CP5632 - Practical
Program to display menu to get valid score, print result, print stars, and quit
"""
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input("Choice: ").upper()
    score = -1
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()

        elif choice == 'P':
            if score == -1:
                print("Get a valid score first")
            else:
                print(determine_result(score))

        elif choice == 'S':
            if score == -1:
                print("Get a valid score first")

            else:
                print_stars(score)
        print()
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell")


def print_stars(score):
    """print stars based on score"""
    for i in range(score):
        print("*", end='')

def get_valid_score():
    """get valid score between 0 and 100"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score

def determine_result(score):
    """returns result based on score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()