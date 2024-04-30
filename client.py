import argparse , socket

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('esperava %d bytes, mas recebeu apenas %d bytes antes do fechamento do socket' % (length, len(data)))
        data += more
    return data


def cliente(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port)) # Inicia o three-way handshake entre o cliente e o servidor
    print('O cliente recebeu um nome de socket', sock.getsockname())
    sock.sendall(b'Enviei, servidor') # Envia os dados. Obs.: Atencao ao conteudo
    reply = recvall(sock, 16)
    print('O servidor diz', repr(reply))
    sock.close()



cliente('127.0.0.1',1025)