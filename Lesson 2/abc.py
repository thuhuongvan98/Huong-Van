a1 = int(input("Nhap a1: "))
a2 = int(input("Nhap a2: "))
b1 = int(input("Nhap b1: "))
b2 = int(input("Nhap b2: "))
c1 = int(input("Nhap c1: "))
c2 = int(input("Nhap c2: "))
c = a2/a1
y=(c1*c-c2)/(c*b1-b2)
x=(c1-y*b1)/a1
print(f"x = {x}, y = {y}")