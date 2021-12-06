# Calculator Project
# this is a new comment for project of my Git course
import math
def addition(number1,number2):
    return "Sum of 2 number are : " + str(number1 + number2)
def subtraction(number1,number2):
    return "subtraction of 2 number are : " + str(number1 - number2)
def multiplication(number1,number2):
    return "multiplication of 2 number are : " + str(number1 * number2)
def division(number1,number2):
    return "division of 2 number are : " + str(number1 / number2)
def dodulus(number1,number2):
    return "dodulus of 2 number are : " + str(number1 % number2)
def exponent(number1,number2):
    return "exponent of 2 number are : " + str(number1 ** number2)
def floor_division(number1,number2):
    return "floor division of 2 number are : " + str(number1 // number2)    
def sqrt(number1,number2):
    sqrt_number1 = math.sqrt(number1)
    sqrt_number2 = math.sqrt(number2)
    return "Square Root of number1 : " + str(sqrt_number1) + " and Square Root number2 : " + str(sqrt_number2) 


number1=float(input("Please enter number 1 : "))
number2=float(input("Please enter number 2 : "))
list_operators = input("Please choose the operator you want : + - * / % //  pow, sqrt,  :  ")

if list_operators == "+":
    print(addition(number1, number2))

elif list_operators == "-":
    print(subtraction(number1, number2))

elif list_operators == "*":
    print(multiplication(number1, number2))

elif list_operators == "/":
    print(division(number1, number2))

elif list_operators == "%":
    print(dodulus(number1, number2))

elif list_operators == "//":
    print(floor_division(number1, number2))

elif list_operators == "pow":
    print(exponent(number1, number2))

elif list_operators == "sqrt":
    print(sqrt(number1, number2))



else:
    print("Please enter a right character 👍")    
