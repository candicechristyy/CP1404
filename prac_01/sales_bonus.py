"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < THRESHOLD :
        p_bonus = 0.10
    elif sales >= THRESHOLD:
        p_bonus = 0.15
    final_bonus = sales * p_bonus
    print(final_bonus)
    sales = float(input("Enter sales: $"))
