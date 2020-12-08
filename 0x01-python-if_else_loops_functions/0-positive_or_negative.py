#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    msg = "is positive"
elif number < 0:
    msg = "is negative"
else:
    msg = "is zero"

print("{} {}".format(number, msg))
