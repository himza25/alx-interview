#!/usr/bin/python3
"""
This module contains a function canUnlockAll which determines if all boxes in
a given list can be unlocked using the keys contained within them. The function
uses an iterative approach to simulate opening boxes
by tracking available keys.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened using keys inside them.

    Args:
    boxes (list of lists of int): Each sublist represents keys inside a box.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    keys = set([0])  # Start with the first box unlocked
    for key in keys:
        keys.update([new_key for new_key in boxes[key]
                     if new_key not in keys and new_key < len(boxes)])

    return len(keys) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False
