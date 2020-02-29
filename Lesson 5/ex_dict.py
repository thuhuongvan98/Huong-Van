teencode = {
    'vk': 'vo', 
    'ck': 'chong', 
    'hoy': 'thoi', 
    'lem': 'lam', 
    'hsi': 'hay sao i',
    'yep': 'yes',
    'choai xu': 'twice'
}
loop = True
while loop:
    key = input('Bạn muốn tra từ gì? ').strip()
    if key in teencode:
        print(f"{key} nghĩa là {teencode[key]}")
    else:
        answer = input('Chưa có trong từ điển. Bạn có muốn thêm mới vào? (yes/no): ').lower().strip()
        if answer == 'yes':
            meaning = input('Mời bạn nhập nghĩa của từ đó: ')
            teencode[key] = meaning
        else:
            pass