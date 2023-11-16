"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE (THIS IS DONE)
from Account import Account

# Define a function for the CD Account
def create_cd_account(cd_balance, cd_interest, cd_maturity):
    """Creates a CD account, calculates interest earned, and updates the account balance.
        Note: Args updated to match modified function names -Brandon Welsh

    Args:
        cd_balance (float): The initial CD account balance.
        cd_interest (float): The APR interest rate for the CD account.
        cd_maturity (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE (DONE)
    cd_account = Account(cd_balance, cd_interest)
    cd_account.set_interest(0)

    return calculate_interest(cd_account, cd_balance, cd_interest, cd_maturity)

    # Calculate interest earned
    # ADD YOUR CODE HERE (DONE)
def calculate_interest(cd_account, cd_balance, cd_interest, cd_maturity):
    interest_earned = cd_balance * (cd_interest/100 * cd_maturity/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE (DONE)
    cd_account.balance += interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE (DONE)
    cd_account.set_balance(cd_account.balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE (DONE)
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return float(cd_account.balance), interest_earned # ADD YOUR CODE HERE (DONE)
