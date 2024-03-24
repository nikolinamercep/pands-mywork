# isEven.py
#this program asks the user to enter a number and then tells the user if the number is even or odd

number = int(input("Enter an integer: "))
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")