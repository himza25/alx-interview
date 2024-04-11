#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    
    :param n: The number of rows in Pascal's triangle
    :type n: int
    :return: A list of lists representing Pascal's triangle
    :rtype: List[List[int]]
    """
    pascal = []  # Initialize an empty list for Pascal's triangle
    if n <= 0:
        return pascal  # Return an empty list if n is not positive
    
    for i in range(n):
        row = [1]  # Start each row with a '1'
        if i > 0:  # For rows beyond the first, calculate intermediate values
            for j in range(1, i):
                # Each element is the sum of the two elements directly above it
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)  # End each row with a '1'
        pascal.append(row)  # Add the completed row to the triangle
    
    return pascal

# This script part is just for testing the function when this script is run directly.
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle in a formatted way.
        """
        for row in triangle:
            print("[{}]".format(", ".join(map(str, row))))

    # Example: Print Pascal's triangle with 5 rows
    print_triangle(pascal_triangle(5))
