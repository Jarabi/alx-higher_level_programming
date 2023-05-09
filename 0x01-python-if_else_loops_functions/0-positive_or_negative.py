#!/usr/bin/python3
import random
number = random.randint(-10, 10)
statement = ""

if number > 0:
    statement = "is positive"
elif number == 0:
    statement = "is zero"
else:
    statement = "is negative"

print(f"{number} {statement}")
