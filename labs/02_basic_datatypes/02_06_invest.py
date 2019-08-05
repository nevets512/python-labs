'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = input("How much will you invest: ")
amount = float(amount)
interest_rate = input("What is the interest rate: ")
interest_rate = float(interest_rate)
years = input("How many years: ")
years = float(years)

future_value = (amount * (1 + (interest_rate))** years)

print(future_value)
