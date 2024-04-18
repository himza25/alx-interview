#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked
using keys found within other boxes. It implements a depth-first search (DFS)
to traverse through the boxes based on the keys each contains.

Usage:
Execute the script to test the canUnlockAll
function with predefined box setups.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened using keys inside them.

    Args:
    boxes (list of lists of int): The list where each element is a list
    of keys in a box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    def dfs(box_index):
        """Recursive function to perform DFS from the given box index."""
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                dfs(key)

    visited = set()
    dfs(0)
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False
