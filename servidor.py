import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 5000
ARQUIVO_SAIDA = 'recebido.pdf'
Pass_correta = "upskill"

# AF_INET stands for Address Family: Internet. Serve para usar ipv4
# SOCK_STREAM tells the socket to use TCP (Transmission Control Protocol).


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

    servidor.bind((HOST, PORT))

    servidor.listen()

    print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

    conexao, endereco = servidor.accept()

    with conexao:

        print(f"Conectado por {endereco}")
        senha_recebida = conexao.recv(1024).decode('utf-8')
        if senha_recebida != Pass_correta:
            print("Senha incorreta. Conexão encerrada.")
            conexao.sendall(b"Senha incorreta! A conexao sera encerrada")
            conexao.close()
        
        conexao.sendall(b"Senha correta. Transferindo arquivo.")
        aes_key = conexao.recv(16)  # 16 bytes for AES-128 key
        print("Chave AES recebida.")
        with open(ARQUIVO_SAIDA, 'wb') as f:
            encrypted_data = b''
            while True:

                dados = conexao.recv(4096)

                if not dados:

                    break
                encrypted_data += dados

            
            cipher = AES.new(aes_key, AES.MODE_ECB)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            with open(ARQUIVO_SAIDA, 'wb') as f:
                f.write(decrypted_data)
        print(f"Arquivo guardado como {ARQUIVO_SAIDA} e desencriptado")