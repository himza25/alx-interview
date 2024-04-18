#!/usr/bin/python3

def canUnlockAll(boxes):
    """ Determine if all boxes can be opened using keys inside them """
    def dfs(box_index):
        """ Perform a depth-first search to check accessible boxes """
        visited.add(box_index)  # Mark this box as visited
        for key in boxes[box_index]:  # Traverse the keys in the current box
            if key not in visited and key < len(boxes):
                dfs(key)  # Recurse if the key opens an unvisited box

    visited = set()  # Track visited boxes
    dfs(0)  # Start DFS from the first box (unlocked)
    return len(visited) == len(boxes)  # Check if all boxes were visited


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [3, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False
