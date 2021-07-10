# 3 slide of triangle
side1 = float(input("Enter Length of Slide 01: "))
side2 = float(input("Enter Length of Slide 02: "))
side3 = float(input("Enter Length of Slide 03: "))

# calculation  semi-perimeter
S_Perimeter = (side1 + side2 + side3) / 2

# calculate area
area = (S_Perimeter*(S_Perimeter-side1) * (S_Perimeter-side2) * (S_Perimeter-side3)) ** 0.5

# output
print(area)