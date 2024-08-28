# Conditional statements with if/elif/else statements
# print('Welcome to the roller-coaster')
# height = int(input('Enter your height in cm: '))
# bill = 0
#
# # >, <, >=, <=, ==. !=
# if height >= 120:
# # print('You can ride the roller-coaster') --> Indentation error
#     print('You can ride the roller-coaster')
#     age = int(input('Enter your age: '))
#     if age <= 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12
#
#     # Check for photos
#     wants_photo = input('Do you want photos(Y/N)? ')
#     if wants_photo == 'Y':
#         bill += 3
#     print(f'Please pay ${bill}')
# else:
#     print('Sorry! You have to grow taller to ride the roller-coaster')

# Modulo operator (%)
# num = int(input('Enter a number: '))
# if num % 2 == 0:
#     print('Even Number')
# else:
#     print('Odd Number')

# # Pizza Order Practise
# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M, and L: ')
# pepperoni = input('Do you want pepperoni (Y/N)? ')
# extra_cheese = input('Do you want extra cheese (Y/N)? ')
# wrong_input = False
#
# bill = 0
#
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# elif size == 'L':
#     bill += 25
# else:
#     wrong_input = True
#     print('You have entered wrong input')
#
# if not wrong_input:
#     if pepperoni == 'Y':
#         if size == 'S':
#             bill += 2
#         else:
#             bill += 3
#     if extra_cheese == 'Y':
#         bill += 1
#
# print(f'Your bill is ${bill}!')

# Logical Operators
# and, or, not
