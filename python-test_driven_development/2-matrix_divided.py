def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
