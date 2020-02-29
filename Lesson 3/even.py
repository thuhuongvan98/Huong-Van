numbers = list(map(int,input("Enter the numbers : ").split(',')))
all_even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        all_even_numbers.append(numbers[i])
    else:
        pass
print("All even numbers: ",all_even_numbers)

x = sum(all_even_numbers)
print("Sum of all even numbers: ",x)

y = 0
for i in range(len(all_even_numbers)):
    y += all_even_numbers[i]
print("hahaha: ",y)
