#!/usr/bin/python

number = int(raw_input("Please enter a number: "))
if number % 4 == 0:
	print("Your number (%r) is divisible by 4.\n") % number
elif number % 2 == 0:
	print("Your number (%r) is even.\n") % number
elif number % 2 != 0:
	print("Your number (%r) is odd.\n") % number

print("Now I will ask for two additional numbers.")
num = int(raw_input("Please enter the first number: "))
check = int(raw_input("Please enter the second number: "))
if num % check == 0:
	print("Your second number evenly divides into your first.\n")
elif num % check != 0:
	print("Your second number does not evenly divide into your first.\n")
