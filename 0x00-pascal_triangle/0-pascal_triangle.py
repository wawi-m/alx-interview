#!/usr/bin/python3
"""Generate Pascal's Triangle based on the sum of adjacent elements."""


def pascal_triangle(n):
    """Generate Pascal's Triangle based on the sum of adjacent elements."""
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
