#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""
import sys
import re


def print_size_errors(size, error_counts):
    """Print the size of all error files and a count of the error types"""
    print('File size: {}'.format(size))
    for k, v in sorted(error_counts.items()):
        print('{}: {}'.format(k, v))


error_counts = {}


if __name__ == '__main__':
    try:
        count = 0
        total_size = 0
        for line in sys.stdin:
            count += 1
            tokens = line.split(' ')
            if len(tokens) >= 2 and re.match('\d.\d.\d.\d', tokens[0]):
                size = int(tokens[-1])
                total_size += size
                error = tokens[-2]
                error_counts[error] = error_counts.get(error, 0) + 1
                if (count % 10 == 0):
                    print_size_errors(total_size, error_counts)
        print_size_errors(total_size, error_counts)
    except KeyboardInterrupt:
                    print_size_errors(total_size, error_counts)
