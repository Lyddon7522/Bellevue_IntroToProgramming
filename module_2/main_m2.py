# Constants
COST_PER_FOOT = 0.87
COST_PER_FOOT_GREATER_100 = 0.80
COST_PER_FOOT_GREATER_250 = 0.70
COST_PER_FOOT_GREATER_500 = 0.50
COMPANY_NAME = "Fast & Fibrous"

def main():
    print(f"Welcome to {COMPANY_NAME} Installation Cost Calculator!")
    print()

    length_of_cable = get_cable_length()

    # Get the cost of the cable per foot depending on the length of cable
    cost_of_cable_per_foot = calculate_bulk_discount_price(length_of_cable)

    cost_of_cable = calculate_cost_of_cable(length_of_cable, cost_of_cable_per_foot)

    #Print the cost of the cable. formate the cost to 2 decimal places
    print(f"The cost for {COMPANY_NAME} to install cable for {length_of_cable:,.2f} feet is ${cost_of_cable:,.2f}. Your invoice is below:")
    print()

    print_invoice(COMPANY_NAME, length_of_cable, cost_of_cable_per_foot, cost_of_cable)

# Get the length of cable from the user
def get_cable_length():
    while True:
        cable_length_needed = input("Enter the length of cable in feet: ")

        try:
            cable_length =  float(cable_length_needed)
            if cable_length <= 0:
                 print("Cable length must be a positive number")
                 print()
                 continue
            return cable_length
        except ValueError:
            print("You entered an invalid number. Please enter a valid number.")
            print()

# Calculate the cost of the cable
def calculate_cost_of_cable(cable_length: float, cost_of_cable_per_foot: float) -> float:
    cost_of_cable = 0

    if cable_length <= 0:
        raise ValueError("Cable length must be a positive number")

    return round (cable_length * cost_of_cable_per_foot, 2)

# Returns the cost of the cable per foot depending on the length of cable. This helps keep the cost calculation DRY and clean
def calculate_bulk_discount_price(cable_length: float) -> float:
    if cable_length > 500:
        return COST_PER_FOOT_GREATER_500
    elif cable_length > 250:
        return COST_PER_FOOT_GREATER_250
    elif cable_length > 100:
        return COST_PER_FOOT_GREATER_100
    else:
        return COST_PER_FOOT


# Print an ASCII invoice
def print_invoice(company_name: str, length_of_cable: float, cost_per_foot: float, total_cost: float) -> None:
    width = 50
    col1_width = 20
    col2_width = 24
    border_width = width - 2  # Width between outer borders

    print("+" + "-" * border_width + "+")
    print(f"|{company_name:^{border_width}}|")
    print("|" + " " * border_width + "|")
    print("+" + "-" * border_width + "+")
    print(f"| {'ITEM':^{col1_width}} | {'DETAILS':^{col2_width - 1}} |")
    print("+" + "-" * (col1_width + 2) + "+" + "-" * (col2_width + 1) + "+")
    print(f"| {'Cable Length':<{col1_width}} | {f'{length_of_cable:,.2f} feet':<{col2_width - 1}} |")
    print(f"| {'Unit Price':<{col1_width}} | {f'${cost_per_foot:,.2f} per foot':<{col2_width - 1}} |")
    print("+" + "-" * (col1_width + 2) + "+" + "-" * (col2_width + 1) + "+")
    print(f"| {'TOTAL':<{col1_width}} | {f'${total_cost:,.2f}':<{col2_width - 1}} |")
    print("+" + "-" * border_width + "+")
    print(f"|{'Thank you for your business!':^{border_width}}|")
    print("+" + "-" * border_width + "+")

if __name__ == "__main__":
    main()