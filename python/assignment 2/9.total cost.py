# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
def calculate_total_cost(quantity, unit_cost):
    total_cost = quantity * unit_cost
    if total_cost > 1000:
        total_cost *= 0.9  # Apply 10% discount
    return total_cost


if __name__ == "__main__":
    unit_cost = 100
    quantity = int(input("Enter the quantity: "))

    total_cost = calculate_total_cost(quantity, unit_cost)
    print(f"Total cost for {quantity} units is: {total_cost}")

