"""Import the Account class and attributes from the Account.py file."""
# ADD YOUR CODE HERE (THIS IS DONE)
from Account import Account

# Define a function for the Savings Account
def create_savings_account(savings_balance, savings_interest, savings_maturity):
    """Creates a savings account, calculates interest earned, and updates the account balance.
        Note: Args updated to match modified function names -Brandon Welsh

    Args:
        savings_balance (float): The initial savings account balance.
        savings_interest (float): The APR interest rate for the savings account.
        savings_maturity (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE (DONE)
    savings_account = Account(savings_balance, savings_interest)
    savings_account.set_interest(0)

    return calculate_interest(savings_account, savings_balance, savings_interest, savings_maturity)

    # Calculate interest earned
     # ADD YOUR CODE HERE (DONE)
def calculate_interest(savings_account, savings_balance, savings_interest, savings_maturity):
    interest_earned = savings_balance * (savings_interest/100 * savings_maturity/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE (DONE)
    savings_account.balance += interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE (DONE)
    savings_account.set_balance(savings_account.balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE (DONE)
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return float(savings_account.balance), interest_earned # ADD YOUR CODE HERE (DONE)
