#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10  # Define the first variable
b = 5   # Define the second variable

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))  # Print the result of addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Print the result of subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Print the result of multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Print the result of division
