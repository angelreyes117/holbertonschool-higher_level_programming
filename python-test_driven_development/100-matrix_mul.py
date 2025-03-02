def matrix_mul(m_a, m_b):
    """Multiplica dos matrices."""
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(type(i) in [int, float] for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(i) in [int, float] for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")
    
    # Verifica que ambas matrices sean rectángulos y que se puedan multiplicar
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[sum(a * b for a, b in zip(m_a_row, m_b_col)) for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return result

