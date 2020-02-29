from random import randint, choice
point = 0
while True:
    a = randint(0,9)
    b = randint(1,9)
    equation = (a+b,a-b,a*b,a/b)
    c = choice(equation)
    d = randint(-1,1)
    if c == a + b:
        print(f"{a} + {b} = {c+d}")
    elif c == a - b:
        print(f"{a} - {b} = {c+d}")
    elif c == a*b:
        print(f"{a} * {b} = {c+d}")
    else:
        print(f"{a} / {b} = {c+d}")
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


