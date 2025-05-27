#!/usr/bin/python3
"""Lazy matrix multiplication using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy's matmul"""
    return np.matmul(m_a, m_b)
