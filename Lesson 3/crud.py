a = input("Welcome to our shop, what do you want (C,R,U,D)? ")
items = ["T-Shirt","Sweater"]
if a == "R":
    print("Our items: ",items)
elif a == "C":
    new = input("Enter new items: ")
    items.append(new)
    print("Our items: ",items)
elif a == "U":
    position = int(input("Update position: "))
    if position <= (len(items)+1):
        update = input("New item: ")
        items[position-1] = update
        print("Our items: ",items)
    else:
        print("No item existed")  
elif a == "D":
    if position <= (len(items)+1):
        delete = int(input("Delete position: "))
        items.remove(items[delete-1])
        print("Our items: ",items)
    else:
        print("No item existed")
else:
    print("Error")