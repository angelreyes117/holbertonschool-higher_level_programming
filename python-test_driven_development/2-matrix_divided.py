def matrix_divided(matrix, div):
    """Divide todos los elementos de una matriz por un número."""
    if type(matrix) is not list or any(type(row) is not list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("matrix can't be empty")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(i / div, 2) for i in row] for row in matrix]

