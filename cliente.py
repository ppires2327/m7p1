import socket
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

HOST = '108.143.76.125'  # Substitua pelo IP do servidor
PORT = 5000
ARQUIVO_ENTRADA = 'exemplo.pdf' # Substitua pelo seu arquivo PDF

Pass_introduzida= input("Insira a palavra-passe: ")

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB)

with open(ARQUIVO_ENTRADA, 'rb') as f:
    file_data = f.read()
    # Pad the data to be multiple of AES block size (16 bytes)
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    cliente.sendall(Pass_introduzida.encode('utf-8'))
    response = cliente.recv(1024).decode('utf-8')
    
    if response == "Senha incorreta! A conexao sera encerrada":
        print("A senha fornecida está incorreta. Tente novamente.")
    else:
        print(response)
        cliente.sendall(key)
        cliente.sendall(encrypted_data)
   
        print(f"Arquivo '{ARQUIVO_ENTRADA}' encriptado e enviado com sucesso.")