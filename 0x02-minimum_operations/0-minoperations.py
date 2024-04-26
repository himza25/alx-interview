#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed .
    """
    if n <= 1:
        return 0
    cnoc = 1  # current number of 'H' characters
    clipboard_size = 1  # size of the clipboard (number of 'H' to paste)
    opNum = 1  # operation count starts with one 'Copy All'
    while cnoc < n:
        if cnoc != 1 and n % cnoc == 0:
            clipboard_size = cnoc  # update clipboard to current 'H' count
            opNum += 1  # perform 'Copy All'
        cnoc += clipboard_size  # perform 'Paste'
        opNum += 1  # increment operation for each paste
    return opNum


if __name__ == "__main__":
    test_cases = [4, 12, 9]
    for case in test_cases:
        result = minOperations(case)
        print(f"Min # of operations for {case} chars: {result}")
