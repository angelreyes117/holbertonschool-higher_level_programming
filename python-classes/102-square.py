#!/usr/bin/python3
"""Defines a Square class with rich comparison operators."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square (default: 0).
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if this square is smaller in area than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square is smaller or equal in area to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if this square is larger in area than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square is larger or equal in area to another."""
        return self.area() >= other.area()
