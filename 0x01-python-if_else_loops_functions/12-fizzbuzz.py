#!/usr/bin/python3

def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            val = 'FizzBuzz'
        elif x % 3 == 0:
            val = 'Fizz'
        elif x % 5 == 0:
            val = 'Buzz'
        else:
            val = x
        print("{}".format(val), end=' ')
