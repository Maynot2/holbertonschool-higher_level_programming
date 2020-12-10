#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(sys.argv)

    print("{} arguments.".format(argc - 1))
    for i in range(len(argv)):
        if i != 0:
            print("{}: {} ".format(i, argv[i]))
