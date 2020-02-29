username = 'hahaha'
password = 'huhuhu'

count = 0
loop = True
loop2 = True
while loop:
    count = count + 1
    if count == 4:
        print("spam vua thoi =))")
        loop = False
    else:
        input_username = input("Username: ")
        if input_username == username:
            while loop2:
                import getpass
                from getpass import getpass
                input_password = getpass()
                if input_password == password:
                    print("Welcome to Cana B Inc.")
                    loop = False
                    loop2 = False
                else:
                    print("Wrong password")
        else:
            print("Wrong username")

