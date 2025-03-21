def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

# Example usage
message = "Hello, World!"
shift_value = 3

encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
decrypted_message = caesar_cipher(encrypted_message, shift_value, mode='decrypt')

print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")