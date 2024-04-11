#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    
    Args:
    n (int): The number of rows to generate.
    
    Returns:
    List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        # Generate middle values by adding two consecutive elements of the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    return triangle

if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print each row of Pascal's triangle in a formatted way.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    # Example usage
    print_triangle(pascal_triangle(5))
