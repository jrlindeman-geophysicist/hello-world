#!/usr/bin/python
import time
name = raw_input("Hi. What is your name? ")
age = int(raw_input("Great! How old are you? "))
lines = int(raw_input("How many times would you like to be told? "))
currentyear = int(time.strftime("%Y"))
age2 = currentyear - age + 100
print((("Good to meet you %r. Since you are %r years old, you will be 100 years old in %r, assuming you were born today or earlier in the year.\n") % (name, age, age2)) * lines)
