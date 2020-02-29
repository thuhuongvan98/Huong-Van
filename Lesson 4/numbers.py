n = int(input("Type a number: "))
numbers = []
for i in range(n):
    numbers.append(i)
print(numbers)

b = int(input("Enter the total number of 1s and 0s: "))
binary = []
if b % 2 == 0:
    x = int(b/2)
else:
    x = int((b-1)/2)
for i in range(x):
        binary.append(1)
        binary.append(0)
if b % 2 == 0:
    pass
else:
    binary. append(1)
print(binary)