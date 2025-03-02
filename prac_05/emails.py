"""
CP1404/CP5632 Practical
Program to store emails and names

Word Occurrences
Estimate: 30 minutes
Actual: 26 minutes
"""

def main():
    """Make dictionary and display emails and names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name(email)
        name_confirmation = input(f"Is your name {full_name}? (Y/n) ").upper()
        if name_confirmation != 'Y' and name_confirmation != '':
            full_name = input("Name: ")

        email_to_name[email] = full_name
        email = input("Email: ")

    print()
    for email, full_name in email_to_name.items():
        print(f"{full_name} ({email})")


def extract_name(email):
    """Extract name from given email"""
    names = email.split('@')[0]
    full_name = " ".join(names.split('.')).title()
    return full_name

main()
