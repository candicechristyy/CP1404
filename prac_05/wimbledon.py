"""
CP1404/CP5632 Practical
Program process and display data from csv file

Word Occurrences
Estimate: 30 minutes
Actual: 28 minutes
"""
def main():
    """Read data from file, make dictionary and display information of champions and countries"""
    lines = get_data()
    champions_to_count = get_champions_count(lines)

    countries = {line.split(',')[1] for line in lines}

    display_champions_and_countries(champions_to_count, countries)


def display_champions_and_countries(champions_to_count, countries):
    """Display results of champions and countries"""
    print("Wimbledon Champions: ")
    for champion, count in champions_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_champions_count(lines):
    """Make dictionary of champions and countries from extracted data"""
    champions_to_count = {}
    for line in lines:
        champion = line.split(',')[2]
        champions_to_count[champion] = champions_to_count.get(champion, 0) + 1
    return champions_to_count


def get_data():
    """Load and return data from csv file"""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        lines = in_file.readlines()
    return lines


main()