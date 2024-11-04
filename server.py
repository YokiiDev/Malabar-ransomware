import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Your key is : ", key)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 4321))
s.listen()

conn, addr = s.accept()
print(addr, ' connected')

msg = conn.recv(2048).decode()
if msg == "key":
    conn.send(key)
    print("Key send !")