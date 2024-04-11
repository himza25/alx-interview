#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    - n (int): The number of rows of the triangle to generate.

    Returns:
    - List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize triangle with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

# Test function
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle in a formatted way.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    # Generate and print Pascal's Triangle for n = 5
    print_triangle(pascal_triangle(5))

