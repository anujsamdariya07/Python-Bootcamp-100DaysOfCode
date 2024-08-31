# For loop
# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#     print(fruit)
#     print(f'{fruit} pie')
#
# print(fruits)

# student_scores = [150, 142, 185, 120, 149, 24, 59, 68, 78, 65]
# total_exam_score = sum(student_scores)
# print(f'Total Exam Score: {total_exam_score}')

# sum = 0
# for score in student_scores:
#     sum += score
# print(f'Total Exam Score (through for loop): {total_exam_score}')

# maximum_score = max(student_scores)
# print(f'Maximum Score: {maximum_score}')
#
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#
# print(f'Maximum Score (through for loop): {max_score}')

# Range function - generates a range of numbers generally used for looping through them
# range(a, b) - numbers from a to b-1
# range(a, b, c) - numbers from a to b-1 with step size of c
# for number in range(1, 10): # 10 not included
#     print(number)
# for number in range(1, 10, 2): # 10 not included with step value of 2
#     print(number)

# printing the sum of all the numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)
