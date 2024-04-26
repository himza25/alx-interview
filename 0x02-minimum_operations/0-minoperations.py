#!/usr/bin/python3
def minOperations(n):
    if n < 2:
        return 0
    operations = 0
    current = n
    for i in range(2, n + 1):
        while current % i == 0:
            operations += i
            current //= i
    return operations


if __name__ == "__main__":
    minOperations_test = __import__('0-minoperations').minOperations
    test_cases = [4, 12]
    for case in test_cases:
        print(f"Min # of operations to reach {case} char: "
              f"{minOperations_test(case)}")
