# div.py
# program that reads in two numbers, divides the first one by the second one and gives the result in an integer and remainder
# author Nikolina
first_number = int(input("Enter first number: "))
second_number = int(input("Enter the number you want to divide by: "))
answer = int(first_number/second_number)
remainder = first_number%second_number
print("{} divided by {} is {} with remainder {}".format(first_number, second_number, answer, remainder))