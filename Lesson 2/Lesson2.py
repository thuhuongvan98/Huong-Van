age = 18
#print(age == 18)
name = "Mai"
if age >= 18 and name == 'Mai':
    print("Welcome to XXX")
elif age == 18:
    print("Đợi thêm 1 năm nữa em êi")
else:
    print("Bố mẹ em đâu?")

#điều kiện của if được xét trước, nếu đúng sẽ k nhắc tới elif
#nếu cả 2 cái đều if sẽ in ra cả 2 vì 2 cái tương đương nhau
#comment: ctrl /
print(bool("")) #rỗng là false, miễn là có kí tự gì thì sẽ là true

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
Delta = b**2 - 4*a*c
if Delta >=0:
    x1 = (-b + Delta**0.5)/(2*a)
    x2 = (-b - Delta**0.5)/(2*a)
    print(f"x1 = {x1}, x2 = {x2}") #f=format, de tranh dau phay
else:
    print("Vo nghiem")