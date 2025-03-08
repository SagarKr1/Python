import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load the private key from the file
file_path = os.path.join(os.getcwd(), "privatekey.pem")
with open(file_path, "rb") as f:
    private_key = RSA.import_key(f.read())

# Create an RSA cipher object
cipher = PKCS1_OAEP.new(private_key)

# Read the encrypted message from the file
encrypted_file_path = os.path.join(os.getcwd(), "encrypted_message.txt")
with open(encrypted_file_path, "rb") as f:
    cipher_text = f.read()

# Decrypt the text
plain_text = cipher.decrypt(cipher_text)

# Save the decrypted data to a file
decrypted_file_path = os.path.join(os.getcwd(), "plain.txt")
with open(decrypted_file_path, "wb") as f:
    f.write(plain_text)
