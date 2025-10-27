import math


def area_rectangle(width, height):
    area = width * height
    return area


def area_circle(radius):
    area = math.pi * radius**2
    return area


def area_triangle(width, height):
    area = width * height / 2
    return area
