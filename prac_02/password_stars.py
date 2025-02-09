"""
CP1404/CP5632 - Practical
Valid password checking program and print asterisks based on password length
"""
MINIMUM_PASSWORD_LENGTH = 8
def main():
    """get valid password and print asterisks based on password length"""
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    """print asterisks based on the length of password"""
    for i in range(len(password)):
        print("*", end='')

def get_password():
    """get valid password that meets the minimum length"""
    password = str(input("Enter password: "))
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid password!")
        password = str(input("Enter password: "))
    return password

main()
