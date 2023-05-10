#!/usr/bin/python3
for ascii_num in range(122, 96, -1):
    if ascii_num % 2 != 0:
        ascii_char = chr(ascii_num - 32)
    else:
        ascii_char = chr(ascii_num)

    print("{}".format(ascii_char), end='')
