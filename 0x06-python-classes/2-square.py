#!usr/bin/python3
"""create a square class"""


class Square():
    """ initiallizing init function """
    
        def _int_(self, size=0):
        """ initiallizing size attribute and making  it to private
        Args:
        size(int): the size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
