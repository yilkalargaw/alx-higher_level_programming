#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdgt = number % 10
else:
    lastdgt = -1 * ((-1 * number) % 10)

if lastdgt > 5:
    print(f"Last digit of {number} is {lastdgt} and is greater than 5")
elif lastdgt == 0:
    print(f"Last digit of {number} is {lastdgt} and is 0")
elif lastdgt < 6 and lastdgt != 0:
    print(f"Last digit of {number} is {lastdgt} and is less than 6 and not 0")
