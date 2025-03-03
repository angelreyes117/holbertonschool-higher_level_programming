#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    
    try:
        return np.matmul(m_a, m_b).tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
