'''

Filename: interview.py
Author: Urquizo, Rafaela
Date: 08/25/36
Instructor: Burgess
'''

print('This program provides the functionality of a simple four-function calculator.')
print('The program will take two user generated numbers, and perform the four basic arithmetic operations')
print('addition, subtraction, multiplication,and division.')
print()
n1 = int(input('Please enter your first number on the line below.\n'))
n2 = int(input('Please enter your second number on the line below.\n'))
print('Addition:')
print(f'The sum of {n1} and {n2} is equal to {n1+n2}')
print()
print('Subtraction:')
print(f'The difference between {n1} and {n2} is equal to {n1 - n2}')
print()
print('Multiplication:')
print(f'The product of {n1} and {n2} is equal to {n1 * n2}')
print()
print('Division:')
print(f'The quotient of {n1} and {n2} is equal to {n1 / n2}')
print()
print('Thank you for using the simple four-function calculator.')
