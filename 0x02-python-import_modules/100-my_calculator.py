#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1.py import add, sub, mul, div

    args = sys.argv[1:]
    arglen = len(args)

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if arglen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        a = int(args[0])
        op = args[1]
        b = int(args[2])
        if operations.get(op, "missing") != missing:
            print("{} {} {} = {}".format(a, op, b, operations[op](a, b)))
        else:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
