import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load the public key from the file
file_path = os.path.join(os.getcwd(), "pubKey.pem")
with open(file_path, "rb") as f:
    public_key = RSA.import_key(f.read())

# Create an RSA cipher object
cipher_rsa = PKCS1_OAEP.new(public_key)

# Text to encrypt
plaintext = "Hello, this is a secret message!"

# Encrypt the text
encrypted_data = cipher_rsa.encrypt(plaintext.encode())

# Save the encrypted data to a file
encrypted_file = os.path.join(os.getcwd(), "encrypted_message.txt")
with open(encrypted_file, "wb") as f:
    f.write(encrypted_data)