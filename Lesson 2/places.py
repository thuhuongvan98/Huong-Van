#list, array
#thao tac lam voi List: C - Create, R - read, U - update, D - delete

places = ["Dai su quan", "Benh vien", "Bai bien","Tau khong gian"] #create


new_place = input("Enter new place plssss... ")
places.append(new_place) #initialize

places[places.index("Dai su quan")] = "Tieu su quan" #update

places.pop() #Neu de blank se auto xoa thg cuoi cung #delete
places.remove("Tau khong gian")
temp = places[0]
places[0] = places[1]
places [1] = temp

print(places[1]) #read
for i in range(len(places)):
    print(places[i])




