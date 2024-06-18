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
    """
    return length * width

def rectangle_perimeter(length, width):
    """!
    Computes a rectangle perimeter

    @param length The rectangle length
    @param width The rectangle width
    @return The rectangle perimeter
    """
    return 2 * (length +  width)

def circle_area(radius):
    """!
    Computes a circle area

    @param radius The circle radius
    @return The circle area
    """
    return math.pi * radius * radius

def circle_circumference(radius):
    """!
    Computes a circle circumference

    @param radius The circle radius
    @return The circle circumference
    """
    return 2 * math.pi * radius
