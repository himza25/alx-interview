#!/usr/bin/python3
"""Prime Game module"""


def count_primes(n):
    """
    Counts primes up to n.
    """
    number = 0
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            number += 1
            for i in range(p, n + 1, p):
                sieve[i] = False
    return number


def isWinner(x, nums):
    """
    Determines game winner.
    """
    players = {"Maria": 0, "Ben": 0}
    for num in nums[:x]:
        count_p = count_primes(num)
        if count_p % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1
    if players['Ben'] > players['Maria']:
        return 'Ben'
    if players['Maria'] > players['Ben']:
        return 'Maria'
    return None
