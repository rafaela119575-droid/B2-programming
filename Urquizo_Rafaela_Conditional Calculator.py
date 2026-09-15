'''

Filename: Conditional calculator.py
Author: Urquizo, Rafaela
Date: 09/10/26
Instructor: Burgess
'''

print('This program provides the functionality of a four-function calculator.')
print('The program will take two user-generated numbers and one of the four basic arithmetic operations')
print('addition, subtraction, multiplication, and division), then perform the desired operation on the')
print('two numbers.')
print()
n1 = int(input('Please enter your first number on the line below.\n'))
print()
print('Please enter your desired operation.')
print('For addition please input: +')
print('For subtraction please input: -')
print('For multiplication please input: *')
print('For division please input: /')
operation=input()
n2 = int(input('Please enter your second number on the line below.\n'))
if operation=='+':
 print('Addition')
 print(f'{n1}+{n2}={n1+n2}')

elif operation == '-':
 print('Subtraction')
 print(f'{n1}-{n2}={n1-n2}')
elif operation == '*':
 print('Multiplication')
 print(f'{n1}*{n2}={n1*n2}')

elif operation == "/":
    if n2 != 0:
     print('Division')
     print(f'{n1}/{n2}={n1/n2}')
    else:
        print("Error: Division by zero is not allowed.")

print('Thank you for using the four-function calculator.')