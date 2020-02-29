name = ["ST","BĐ","BTL","CG","DD","HBT"]
population = [150300,247100,333300,266800,420900,318000]

a = max(population)
print("Quận có đông dân số nhất là:", name[population.index(a)], f"với {a} người")

b = min(population)
print("Quận có ít dân số nhất là:", name[population.index(b)], f"với {b} người")

area = [117.43,9.224,43.35,12.04,9.96,10.09]

density = []
for i in range(len(area)):
    d = population[i]/area[i]
    density.append(d)
print(density)

avgden = sum(density)/len(density)
print(avgden)