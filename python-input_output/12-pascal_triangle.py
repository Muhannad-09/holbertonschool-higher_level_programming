#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n rows.

    Args:
        n (int): Number of rows of Pascal's triangle.

    Returns:
        list: A list of lists, each inner list is a row in the triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            # Sum of two adjacent elements in the previous row
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
