#person = ['Duc', 96, 'Ha Noi', 'Son La', 'dev', False, True]

person = {
    'name': 'Duc', 
    'YOB': 96, 
    'address': 'Hanoi'
}

#READ

print(person['name'])

a = person['name']

for key, value in person.items(): #() = read all
    print(key, value)

print('job' in person)
print('name' in person) #ktra xem có trong dict hay không (T/F)

if 'name' in person:
    print(person['name'])

#CREATE
person['gender'] = 'male'

#UPDATE
person['address'] = 'Dalat'

#DELETE
del person['YOB']

print(person)