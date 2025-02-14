# 1.
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3.
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
    print(first_number + second_number)

# 4.
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)

