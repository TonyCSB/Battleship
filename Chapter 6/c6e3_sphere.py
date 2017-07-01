# c6e3_sphere.py
# Tony Chen

from math import *

def sphereArea(radius):
    area = 4 * pi * radius ** 2
    return area

def sphereVolume(radius):
    volume = 4 / 3 * pi * radius ** 3
    return volume

def main():
    print("This program calculates the volume and surface area of")
    print("a sphere from its radius, given as input.\n")

    r = float(input("Radius? "))

    print()

    area = sphereArea(r)
    volume = sphereVolume(r)

    print("The volume of the sphere is: {0:0.2f}.".format(volume))
    print("The area of the sphere is: {0:0.2f}.".format(area))

main()
