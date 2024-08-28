# Tip Calculator

# Calculating total bill
total_bill = float(input('What was the total bill? $'))

# Percentage of tip
percentage_tip = float(input('How much tip would you like to give? '))

# No. of people splitting the bill
no_of_people = float(input('How many people to split the bill? '))

# Answer
answer = round((total_bill + ((percentage_tip/100) * total_bill)) / no_of_people, 2)
print(f'Each person should pay: ${answer}')
