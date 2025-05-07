import socket

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 5000
ARQUIVO_SAIDA = 'recebido.pdf'

# AF_INET stands for Address Family: Internet. Serve para usar ipv4
# SOCK_STREAM tells the socket to use TCP (Transmission Control Protocol).

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    
        servidor.bind((HOST, PORT))
    
        servidor.listen()
    
        print(f"Servidor aguardando conexões em {HOST}:{PORT}...")


    
        conexao, endereco = servidor.accept()
    
        with conexao:
    
            print(f"Conectado por {endereco}")
    
            with open(ARQUIVO_SAIDA, 'wb') as f:
    
                while True:
    
                    dados = conexao.recv(4096)
    
                    if not dados:
    
                        break
    
                    f.write(dados)


    
            print(f"Arquivo salvo como {ARQUIVO_SAIDA}")