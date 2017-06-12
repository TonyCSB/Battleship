# c3e1_sphere.py
# Tony Chen

def main():
    print("This program calculates the volume and surface area")
    print("of a sphere, given its radius.")
    
    import math
    r = float(input("Please enter the radius of the sphere: "))

    volume = 4 / 3 * math.pi * r ** 3
    surfaceArea = 4 * math.pi * r ** 2
    
    print("The volume of the sphere is", volume,)
    print("The surface area of the sphere is", surfaceArea)

main()
