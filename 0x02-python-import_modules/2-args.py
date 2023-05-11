#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av

    len_av = len(av)

    if len_av > 2:
        print("{} arguments:".format(len_av - 1))

        for i in range(1, len_av):
            print("{}: {}".format(i, av[i]))
    elif len_av == 2:
        print("1 argument:")
        print("{}: {}".format(len_av - 1, av[1]))
    else:
        print("0 arguments.")
