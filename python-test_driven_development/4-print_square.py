def print_square(size):
    """Imprime un cuadrado de tamaño especificado con el carácter '#'."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)

