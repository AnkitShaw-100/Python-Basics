class Loan:
    def __init__(self, principal, rate_of_interest, duration):
        self.principal = principal
        self.rate_of_interest = rate_of_interest
        self.duration = duration
    
    def calculate_maturity_value(self):
        # Calculate the maturity value using the formula: M = P * (1 + (r/100)) ^ t
        maturity_value = self.principal * ((1 + (self.rate_of_interest / 100)) ** self.duration)
        return maturity_value

# Get user input for principal, rate of interest, and duration
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (as a percentage): "))
duration = int(input("Enter the duration (in years): "))

# Create a Loan object with the provided values
loan = Loan(principal, rate_of_interest, duration)

# Calculate and display the maturity value
maturity_value = loan.calculate_maturity_value()
print(f"The maturity value of the loan is: {maturity_value:.2f}")
