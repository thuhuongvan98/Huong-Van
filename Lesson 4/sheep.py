sheep = [10, 30, 56, 240, 150, 98, 111]

print("Hello my name is Huong and these are my sheep's size",sheep)

for a in range(4):
    print("MONTH ",a+1)
    for i in range(len(sheep)):
        sheep[i] = sheep[i]+50
    print(f"After 1 month, here is my flock now {sheep}")
    shear = max(sheep)
    print(f"Now my biggest sheep has size {shear}. Let's shear it!")
    sheep[sheep.index(shear)] = 8
    print(f"After shearing here is my flock now {sheep}")

print(f"In total, my flock has size {sum(sheep)}")
print(f"I would get {sum(sheep)} * $2 = ${sum(sheep)*2}")