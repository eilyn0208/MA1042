"""# with the print( )  function we display text on the screen
print("***Welcome to the savings calculator***")

# we use the input() function to enter data with the keyboard and assign it to the variable name
print("Enter your name:")
name = input()

# we use the float() function to convert text to decimal number and int() to integer number
initial_balance = float(input("Enter your initial balance: "))
final_balance = float(input("Enter your final balance: "))
months = int(input("Enter the number of months you want to save: "))

# we then calculate the savings
savings = (final_balance - initial_balance) / months

# We use the round() function to round the results to zero decimal places.
print(f"{name}, if you want to have a final savings of ${round(final_balance, 0)} you must save ${round(savings, 0)} during {months} months")
"""
print("***Welcome to the savings calculator***")
print("Enter your name:")
name = input()
initial_balance = float(input("Enter your initial balance: "))
final_balance = float(input("Enter your final balance: "))
months = int(input("Enter the number of months you want to save: "))    
savings = (final_balance - initial_balance) / months
print(f"{name}, if you want to have a final savings of ${round(final_balance, 0)} you must save ${round(savings, 0)} each month for {months} months")