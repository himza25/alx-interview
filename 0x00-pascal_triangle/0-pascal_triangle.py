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
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        # Calculate the middle values as sums of two consecutive numbers from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)
    
    return triangle

# Test function to ensure it meets the requirements
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle in a formatted way.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
