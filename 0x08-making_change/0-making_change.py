#!/usr/bin/python3
"""
Change comes from within
"""

def help(start, end, coins, total, number, time, memo):
    """
    Backtracking recursion with memoization
    to find the number of coins.
    """
    if (start, number) in memo:
        return memo[(start, number)]
    
    if start > end:
        return float('inf')
    
    while coins[start] + number <= total:
        number += coins[start]
        time += 1

    if number == total:
        return time
    
    include = help(start, end, coins, total, number, time, memo)
    exclude = help(start + 1, end, coins, total, number, time, memo)
    
    memo[(start, number)] = min(include, exclude)
    return memo[(start, number)]

def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0
    
    sorted_coins = sorted(coins, reverse=True)
    result = help(0, len(sorted_coins) - 1, sorted_coins, total, 0, 0, {})
    return result if result != float('inf') else -1

if __name__ == "__main__":
    # Main file for testing
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

