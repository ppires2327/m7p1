import socket
import os

HOST = '68.221.132.42'  # Substitua pelo IP do servidor
PORT = 5000
ARQUIVO_ENTRADA = 'exemplo.pdf'  # Substitua pelo seu arquivo PDF
Pass_correta = "upskill"

Pass_introduzida= input("Insira a palavra-passe: ")

if Pass_introduzida == Pass_correta:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        with open(ARQUIVO_ENTRADA, 'rb') as f:
            dados = f.read()
            cliente.sendall(dados)

    print(f"Arquivo '{ARQUIVO_ENTRADA}' enviado com sucesso.")