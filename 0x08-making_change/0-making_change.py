#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Args:
        coins (list of int): Coin values.
        total (int): Amount to be made.

    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize DP table with a large value representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Update DP table

    return dp[total] if dp[total] != float('inf') else -1  # Return result


if __name__ == "__main__":
    # Main file for testing
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
