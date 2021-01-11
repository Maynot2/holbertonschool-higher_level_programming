#!/usr/bin/python3
"""Implementation of the N queen problem with backtracking algorythm"""
import sys


def is_safe(q1, q2):
    """Checks ia queen is safe ie not under attack by another queen (same row,
    same column, same diagonal)
    """
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except:
        print('N must be a number')
        sys.exit(1)
    if size < 4:
        print('N must be at least 4')
        sys.exit(1)
