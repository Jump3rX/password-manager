from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter master password: ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key',"wb") as key_file:
#         key_file.write(key)


def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("Account:",user)
            print("Password:",fer.decrypt(passw.encode()).decode())

def add():
    account = input("Account: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(account + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    choice = input("Would you like to add or view a password (view or add)? or type Q to quit: ").lower()

    if choice == "q":
        break

    if choice  == "add":
        add()
    elif choice == "view":
        view()
    else:
        print("Invalid choice!")
        continue