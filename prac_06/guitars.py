from prac_06.guitar import Guitar

guitars =[]
print("My guitars!")
name = str(input("Name: "))
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_data = Guitar(name, year, cost)
    print(f"{guitar_data} added.")
    guitars.append(guitar_data)
    name = str(input("Name: "))

max_name_length = max(len(guitar.name) for guitar in guitars)
max_cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string =  "(vintage)"
    print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:{max_cost_length},.2f}{vintage_string}")
