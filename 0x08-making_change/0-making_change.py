#!/usr/bin/python3
"""
Change comes from within
"""

def help(start, end, coins, total, number, time):
    """
    Backtracking recursion to find the number of coins.
    """
    if start > end:
        return -1
    while coins[start] + number <= total:
        number += coins[start]
        time += 1
    if number == total:
        return time
    return help(start + 1, end, coins, total, number, time)

def makeChange(coins, total):
    """
    Find the fewest number of coins needed to meet total.
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    return help(0, len(sorted_coins) - 1, sorted_coins, total, 0, 0)

if __name__ == "__main__":
    # Main file for testing
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
