#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Multiplies two matrices without using external libraries."""
    
    # Input validation
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if not m_a or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    
    # Validate multiplication dimensions
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = [[sum(m_a[i][k] * m_b[k][j] for k in range(cols_a)) 
               for j in range(len(m_b[0]))] for i in range(len(m_a))]
    
    return result
