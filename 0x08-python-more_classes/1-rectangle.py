#!/usr/bin/python3

"""A class Rectangle representing a Rectangle"""

class Rectangle():
    """creating int function for the class rectangle"""

    def __init__(self, width=0, height=0):

        """setting the Rctangle variables"""

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            """

            self.width = width
            self.height = height

            @property
            def width(self):
                """return the width of the rectangle"""
                return self.__width

            @width.setter
            def width(self, value):
                if type value is not int(value, int):
                    raise TypeError("width must be an integer")
                if value < 0:
                    raise ValueError("width must be >= 0")

                self.__width = value

            @property
            def height(self):
                """return the height of the rectangle """
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")

                self.__height = value:
