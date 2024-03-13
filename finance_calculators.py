import math

# provide the below piece of information to the user using print function 
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("")
# request user to enter an option from the above menu using an input function inorder to proceed
user_option = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()


if (user_option == "investment"):
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing for: "))
    interest_type = (input("Do you want 'simple' or 'compound' interest? ")).lower()

    r = interest_rate / 100

    if (interest_type == "simple"):
        total_amount = amount * (1 + r * years)

    elif (interest_type == "compound"):
        total_amount = amount * math.pow((1 + r),years)

    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

    print(f"The total amount after {years} years at {interest_rate}% {interest_type} interest will be: £{total_amount:.2f}")


elif (user_option == "bond"):
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months for bond repayment: "))

    i = ((interest_rate / 100) / 12)

    monthly_repayment = (i * house_value) / (1 - (1 + i)**(- months))

    print(f"The monthly repayment for the bond will be: £{monthly_repayment:.2f}")


else:
    print("Invalid entry. Please enter 'investment' or 'bond'.")

