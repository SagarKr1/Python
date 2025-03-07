from pwn import *

p = process(
    [
        "python3",
        "-c",
        'print("Enter your name:"); name = input(); print("Hello,", name)',
    ]
)
p.sendline(b"Alice")
print(p.recv().decode())


# import socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 1234))
# server.listen(1)
# print("Listening on port 1234...")
# conn, addr = server.accept()
# print(f"Connection from {addr}")
# conn.send(b"Welcome! Enter your name:\n")
# name = conn.recv(1024).decode().strip()
# response = f"Hello, {name}\n"
# print(f"Sending response to client: {response}")  
# conn.send(response.encode())
# conn.close()
# server.close()
