from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Input the password
password = input("Password: ").encode()

# Generate a random 16-byte key (in a real app, use a key derived from a master password)
key = get_random_bytes(16)

# Generate a random 16-byte IV (Initialization Vector)
iv = get_random_bytes(16)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad and encrypt the password. pad() ensures the password is the correct length.
ciphertext = cipher.encrypt(pad(password, AES.block_size))

# Write IV + ciphertext to the file in binary mode
with open("bd.txt", "wb") as file:
    file.write(iv + ciphertext)

print("Password encrypted and saved.")