import os
from Crypto.PublicKey import RSA

# Generate a 3072-bit RSA key pair
mykey = RSA.generate(3072)

# Define the file path in the same folder as the script
file = os.path.join(os.getcwd(), "pubKey.pem")

# Export the public key to the file
with open(file, "wb") as f:
    f.write(mykey.publickey().exportKey())
