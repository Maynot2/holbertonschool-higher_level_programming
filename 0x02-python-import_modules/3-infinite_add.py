#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    args = map(int, args)
    print(sum(args) if args else 0)
