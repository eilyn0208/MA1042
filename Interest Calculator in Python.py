"""
print("***Welcome to the Interest Calculator***")

# assign values to the required variables
interest_rate = 0.08
accumulated_interest = 0
name = input("Enter your name: ")
balance = int(input("Enter your initial balance: "))
deposit = int(input("Enter an amount to be deposited in October: "))
withdrawal = int(input("Enter an amount to withdraw in December: "))

# we use a for loop to calculate the interest and the monthly balance
for month in range(1, 12 + 1):
 
     #calculate the monthly interest and add it to the interest and balance accumulators
     monthly_interest = balance * interest_rate / 12
     accumulated_interest = accumulated_interest + monthly_interest
     balance = balance + monthly_interest

     # we evaluate if the month is October to make a deposit and December to make a withdrawal
     if month == 10:
          balance = balance + deposit

     if month == 12:
          balance = balance - withdrawal

     print(f"Balance in month {month} is ${round(balance, 0)}")

print(f"The balance at the end of the year in the investment account will be: ${round(balance, 0)}")
print(f"The interest earned in one year will be: ${round(accumulated_interest, 0)}")
"""
print("***Welcome to the Interest Calculator***")
print("Enter your name: ")
name= input()
print("Enter your initial balance: ")
balance= int(input())
deposit = int(input("Enter an amount to be deposited in October: "))
withdrawal = int(input("Enter an amount to withdraw in December: "))

#calculate interest
interest_rate = 0.08
accumulated_interest = 0
for month in range(1, 13):
    monthly_interest = balance * interest_rate / 12
    accumulated_interest = accumulated_interest + monthly_interest
    balance = balance + monthly_interest

    if month == 10:
        balance = balance + deposit
    if month == 12:
        balance = balance - withdrawal
    print(f"Balance in month {month} is ${round(balance, 0)}")

print(f"The balance at the end of the year in the investment account will be: ${round(balance, 0)}")
print(f"The interest earned in one year will be: ${round(accumulated_interest, 0)}")