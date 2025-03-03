def print_square(size):
    """
    Prints a square with the character '#'
    """
    if not isinstance(size, int) or size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
