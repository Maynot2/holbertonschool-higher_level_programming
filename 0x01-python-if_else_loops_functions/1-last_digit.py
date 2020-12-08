#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number == 0:
    print("Last digit of {} is 0".format(number))
else:
    last_digit = int(str(number)[-1]) * abs(number)//number

    if last_digit > 5:
        msg = "greater than 5"
    elif last_digit == 0:
        msg = "0"
    else:
        msg = "less than 6 and not 0"

    print("Last digit of {} is {} and is {}".format(number, last_digit, msg))
