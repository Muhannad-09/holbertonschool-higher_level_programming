#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    # Check if m_a and m_b are lists of lists (i.e., matrices)
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Ensure the matrices can be multiplied: columns of m_a == rows of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Use NumPy's matmul function to perform matrix multiplication
    result = np.matmul(m_a, m_b)

    return result.tolist()  # Convert the result back to a Python list
