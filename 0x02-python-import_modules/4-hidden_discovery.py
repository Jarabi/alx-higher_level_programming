#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as h4

    # Use dir() to get list of names in file
    names = dir(h4)

    for name in names:
        if name[:2] == '__' or name[-2:] == '--':
            continue
        print(name)
