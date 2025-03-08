#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
