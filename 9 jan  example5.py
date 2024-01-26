# 9 jan 24 example3
print("check 3 sides of triangle")
a=(int(input("enter 1 side")))
b=(int(input("enter 2 side")))
c=(int(input("enter 3 side")))
if (a == b and b == c):
    print("equilateral")
elif(a == b or b == c or a ==c):
    print("isosceles")
elif(a != b and b != c):
    print("scalene")

