from calculation import calculate #nếu k nằm trong cùng folder thì tên file phải là Lesson6.calculation
from random import randint
point = 0
print("BEGINNER")

while True:
    import random
    a = randint(0,9)
    b = randint(1,9)
    if point < 5:
        equation = list('+')
    elif point == 5:
        print("ADVANCED")
        equation.append('-')
        equation.append('*')
        equation.append('/')
    c = random.choice(equation)
    d = randint(-1,1)
    z = calculate(a,b,c)
    print(f"{a} {c} {b} = {z+d}")
    user_answer = input("Is this equation true or false? (T/F): ")
    if d == 0:
        if user_answer == "T":
            print("You are correct!")
            point = point + 1
        else:
            print("You are wrong!")
    else:
        if user_answer == "T":
            print("You are wrong!")
        else:
            print("You are correct!")
            point = point + 1
    print("Your point is: ",point)

    



