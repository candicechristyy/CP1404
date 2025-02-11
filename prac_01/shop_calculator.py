P_DISCOUNT = 0.10
item_quantity = int(input("Number of items: "))
while item_quantity < 0:
    print("Invalid number of items!")
    item_quantity = int(input("Number of items: "))
total_price = 0
for i in range(item_quantity):
    item_price = float(input("Price of time: "))
    total_price += item_price
if total_price > 100:
   discount_value = P_DISCOUNT * total_price
   total_price -= discount_value
print(f"Total price for {item_quantity} items is ${total_price:.2f}")