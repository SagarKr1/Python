enc_message = "L|kÇy+*^⌂*zo⌂é*Çkvsno|*kÇom*vo*zk}}*cyvksr⌂¶"

for a in range(0, 256):
    
    pw = ""
    for i in enc_message:
        de = chr(ord(i) - a)
        pw += de
    print(f"-{a} PW = ", pw)
    
    pwd = ""
    for i in enc_message:
        de = chr(ord(i) + a)
        pwd += de
    print(f"{a} PWD = ", pwd)

# pwd = "Yolaih⋸¬"
# for char in pwd:
#     print(f"Character: {char}, Unicode: {ord(char)}")