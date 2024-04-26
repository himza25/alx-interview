#!/usr/bin/python3
"""Calculates minimum operations to reach n 'H' characters using "Copy All"
and "Paste".
"""


def min_operations(n):
    """Returns min number of operations to produce n"""
    if n < 2:
        return 0
    operations = 0
    current = n
    for i in range(2, int(n**0.5) + 1):
        while current % i == 0:
            operations += i
            current //= i
    if current > 1:
        operations += current
    return operations


if __name__ == "__main__":
    test_cases = [4, 12]
    for case in test_cases:
        print(f"Min # of operations to reach {case} characters: "
              f"{min_operations(case)}")
