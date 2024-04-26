#!/usr/bin/python3
"""Minimum operations using 'Copy All' and 'Paste'"""


def min_operations(n):
    """Calculate minimum operations to produce exactly n 'H' chars."""
    if n <= 1:
        return 0
    current_h_count = 1
    clipboard_size = 1
    operations = 1  # Start with one 'Copy All'
    while current_h_count < n:
        if current_h_count != 1 and n % current_h_count == 0:
            clipboard_size = current_h_count
            operations += 1  # Perform 'Copy All'
        current_h_count += clipboard_size
        operations += 1  # Perform 'Paste'
    return operations


if __name__ == "__main__":
    test_cases = [4, 12, 9]
    for case in test_cases:
        result = min_operations(case)
        print(f"Min # of operations for {case} chars: {result}")
