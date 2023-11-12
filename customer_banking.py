# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

dashes = "-" * 30

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    #NOTE: add a loop to check if input is valid, but only once you have this working
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings interest rate (whole numbers. if 5%, type 5): "))
    savings_maturity = int(input("Enter the number of months for savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(dashes)
    print(f"Interest earned on savings account: {interest_earned:.2f}")
    print(f"Updated savings account balance with interest earned: {updated_savings_balance:.2f}")
    print(dashes)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    #NOTE: add a loop to check if input is valid, but only once you have this working
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD interest rate (whole numbers. if 5%, type 5): "))
    cd_maturity = int(input("Enter the number of months for CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(dashes)
    print(f"Interest earned on CD account: {interest_earned:.2f}")
    print(f"Updated CD account balance with interest earned: {updated_cd_balance:.2f}")
    print(dashes)

if __name__ == "__main__":
    main()
    # Call the main function.
