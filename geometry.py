"""!
@file geometry.py
@brief This module provides mathematical operations
"""

import math

def rectangle_area(length, width):
    """!
    Computes a rectangle area

    @param length The rectangle length
    @param width The rectangle width
    @return The rectangle area
    @exception ValueError Raised when length or width is less than 1
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length or width cannot be zero or negative")
    return length * width

def rectangle_perimeter(length, width):
    """!
    Computes a rectangle perimeter

    @param length The rectangle length
    @param width The rectangle width
    @return The rectangle perimeter
    @exception ValueError Raised when length or width is less than 1
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length or width cannot be zero or negative")
    return 2 * (length +  width)

def circle_area(radius):
    """!
    Computes a circle area

    @param radius The circle radius
    @return The circle area
    @exception ValueError Raised when radius is less than 1
    """
    if radius < 1:
        raise ValueError("Radius cannot be null or negative")

    return math.pi * radius * radius

def circle_circumference(radius):
    """!
    Computes a circle circumference

    @param radius The circle radius
    @return The circle circumference
    @exception ValueError Raised when radius is less than 1
    """
    if radius < 1:
        raise ValueError("Radius cannot be null or negative")
    return 2 * math.pi * radius
