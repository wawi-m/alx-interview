#!/usr/bin/python3
"""Generate Pascal's Triangle based on the sum of adjacent elements."""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        
        # Calculate the values in the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)  # Append the row to the triangle
    
    return triangle

def sum_of_row(row):
    """Calculate the sum of a given row in Pascal's Triangle."""
    return sum(row)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    triangle = pascal_triangle(n)
    
    for row in triangle:
        print(row)
    
    # Validate the sum property
    for i in range(n):
        row_sum = sum_of_row(triangle[i])
        expected_sum = 2 ** i
        print(f"Sum of row {i}: {row_sum}, Expected: {expected_sum}")
