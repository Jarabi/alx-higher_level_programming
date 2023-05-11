#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5

_sum = add(a, b)
_diff = sub(a, b)
_prod = mul(a, b)
_quot = div(a, b)
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, _sum))
    print("{:d} - {:d} = {:d}".format(a, b, _diff))
    print("{:d} * {:d} = {:d}".format(a, b, _prod))
    print("{:d} / {:d} = {:d}".format(a, b, _quot))
