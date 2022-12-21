#!/usr/bin/python3
"""creating a square class """


class Square():
    """ defining the square """

    def __init__(self, size):
        """ initializing the size attribute and making it private
        Args:
        size: the size of the square
        """
        self.__size = size
