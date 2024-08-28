# Subscripting
# print('Hello'[-1])

# String
# print('123' + '345')

# Integer
# print(123 + 345)

# Large numbers
# print(123, 456, 789) --> in normal language
# print(123_456_789)

# Float
# print(3.14)

# Boolean
# print(True)

# len(1234) --> Type error

# Type checking
# print(type('Hello')) # <class 'str'>
# print(type(132)) # <class 'int'>
# print(type(132.5)) # <class 'float'>
# print(type(True)) # <class 'bool'>

# Type conversion
# num = '123'
# print(type(num))
# num = int(num)
# print(type(num))

# int()
# float()
# str()
# bool()

# ValueError
# print(int('abc') + int('345'))

# TypeError: can only concatenate str (not "int") to str
# print('Number of letters in your name: ' + len(input("Enter your name: ")))
# print('Number of letters in your name: ' + str(len(input("Enter your name: "))))

# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(8 / 3)
# print(8 // 3) # Integer division
# print(2 ** 10) # Exponential function

# PEMDAS - Parentheses, exponents, multiplication / division, addition / subtraction

# Rounding numbers
# print(70 / 1.84**2)
# print(round(70 / 1.84**2))
# print(round(70 / 1.84**2, 2)) # round to 2 decimal places

# Number manipulation
score = 0
# print(score)
score += 1
# print(score)

# f-strings
print(str(True) + ', you are winning' + '. Your score is ' + str(score))
print(f'{True}, you are winning. Your score is {score}')
