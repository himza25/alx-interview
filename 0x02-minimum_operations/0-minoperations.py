#!/usr/bin/python3
"""Minimum operations using "Copy All" and "Paste"."""


def min_operations(n):
    """Calculate minimum operations to produce exactly n 'H' chars."""
    if n < 2:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations


if __name__ == "__main__":
    test_cases = [4, 12, 9]
    for case in test_cases:
        result = min_operations(case)
        print(f"Min # of operations for {case} chars: {result}")
