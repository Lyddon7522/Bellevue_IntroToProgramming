def main():
    print("Investment Calculator")
    print("This program calculates the future value of an investment and how long it takes to double.")

    # Get the interest rate
    interest_rate = get_interest_rate_input()

    # Get the initial investment amount
    initial_investment = get_investment_amount_input()

    # Generate the investment schedule
    schedule_data = generate_investment_schedule(initial_investment, interest_rate)

    # Calculate the years to double the investment
    years = len(schedule_data)

    # Display the result
    print()
    print(f"It will take {years} years for an investment of ${initial_investment:,.2f} to double at an interest rate of {interest_rate}%.")

    # Display the schedule table
    print_investment_schedule(schedule_data)

def generate_investment_schedule(initial_investment, interest_rate):
    interest_rate_decimal = interest_rate / 100
    current_amount = initial_investment
    target_amount = initial_investment * 2
    schedule_data = []

    while current_amount < target_amount:
        beginning_balance = current_amount
        interest_earned = beginning_balance * interest_rate_decimal
        current_amount += interest_earned

        schedule_data.append({
            'year': len(schedule_data) + 1,
            'beginning_balance': beginning_balance,
            'interest_earned': interest_earned,
            'ending_balance': current_amount
        })

    return schedule_data

def print_investment_schedule(schedule_data):
    print()
    print("Yearly Growth Schedule")
    print("-" * 76)
    print(f"{'Year':^8} | {'Beginning Balance':^20} | {'Interest Earned':^20} | {'Ending Balance':^20}")
    print("-" * 76)

    for data in schedule_data:
        year = f"{data['year']:^8}"
        beginning = f"${data['beginning_balance']:,.2f}".center(20)
        interest = f"${data['interest_earned']:,.2f}".center(20)
        ending = f"${data['ending_balance']:,.2f}".center(20)
        print(f"{year} | {beginning} | {interest} | {ending}")

    print("-" * 76)

def get_interest_rate_input():
    while True:
        try:
            interest_rate = float(input("Enter the interest rate as a percentage (e.g., 5 for 5%): "))
            if interest_rate <= 0 or interest_rate > 100:
                print("Invalid interest rate. Enter a value between 0 and 100.")
                print()
                continue
            return interest_rate
        except ValueError:
            print("Invalid interest rate. Enter a valid number.")

def get_investment_amount_input():
    while True:
        try:
            initial_investment = float(input("Enter the initial investment amount: $"))
            if initial_investment <= 0:
                print("Invalid investment amount. Enter a positive number.")
                print()
                continue
            return initial_investment
        except ValueError:
            print("Invalid investment amount. Enter a valid number.")

if __name__ == "__main__":
    main()