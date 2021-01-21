#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""
import sys
import re


def print_size_errors(size, error_counts):
    """Print the size of all error files and a count of the error types"""
    print('File size: {}'.format(size))
    for k, v in sorted(error_counts.items()):
        if v:
            print('{}: {}'.format(k, v))


def is_valid_line(line):
    """Check if line is a valid request"""
    regex = '.+ \d+'
    return not not re.match(regex, line)


error_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


if __name__ == '__main__':
    try:
        count = 0
        total_size = 0
        for line in sys.stdin:
            count += 1
            tokens = line.split(' ')
            if is_valid_line(line):
                size = int(tokens[-1])
                total_size += size
                error = tokens[-2]
                if error in error_counts.keys():
                    error_counts[error] += 1
                if (count % 10 == 0):
                    print_size_errors(total_size, error_counts)
        print_size_errors(total_size, error_counts)
    except KeyboardInterrupt:
                    print_size_errors(total_size, error_counts)
