a = int(input("Please enter a number: "))
number = 0
for x in range(1,a+1):
    for y in range(1,a+1):
        number = x * y
        print('{:<5}'.format(number), end='')
    print()

a = int(input("Please enter a number: "))

number = 0

for x in range(1,a+1):
    if x % 2 == 0:
        for y in range(1,a+1):
            if y % 2 == 0:
                number = 0
            else:
                number = 1
            print('{:<3}'.format(number),end='')
    else:
        for y in range(1,a+1):
            if y % 2 == 0:
                number = 1
            else:
                number = 0
            print('{:<3}'.format(number),end='')
    print()
    


