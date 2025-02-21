"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_subject_details(data)

def print_subject_details(data):
    """display subject details from data"""
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]:<12} and has {parts[2]:>3} students")

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    merged_parts = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        merged_parts.append(parts)
    input_file.close()
    return merged_parts  # See if that worked



main()