import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('Welcome to PyPassword Generator!')
nr_letters = int(input('Enter the no. of letters that you want: '))
nr_symbols = int(input('Enter the no. of symbols that you want: '))
nr_numbers = int(input('Enter the no. of numbers that you want: '))

password_list = []
for num in range(0, nr_letters):
    random_number = random.randint(0, len(letters)-1)
    password_list.append(letters[random_number])

for num in range(0, nr_symbols):
    random_number = random.randint(0, len(symbols)-1)
    password_list.append(symbols[random_number])

for num in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers)-1)
    password_list.append(numbers[random_number])

password = ''
for num in range(0, len(password_list)):
    random_number = random.randint(0, len(password_list)-1)
    password += password_list[random_number]

print(f'Your Password is: {password}')
