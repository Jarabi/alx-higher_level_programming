#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0
    arg_len = len(argv)

    if (arg_len == 1):
        pass
    else:
        for k in range(1, arg_len):
            total += int(argv[k])
    print(total)
