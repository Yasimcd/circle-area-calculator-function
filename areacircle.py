#A simple function that returns the area of a circle of a given radius.
import math

def area_circle(radius):
  r = int(input("Enter radius to solve for area of a circle: "))
  a = math.pi * r**2
  print(round(a, 2))

area_circle(1) 