import argparse , socket

def recvall(conn, length):
    data = b''
    while len(data) < length:
        more = conn.recv(length - len(data))
        if not more:
            raise EOFError('esperava %d bytes, mas recebeu apenas %d bytes antes do fechamento do socket' % (length, len(data)))
        data += more
    return data


def servidor(porta):
    sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', porta))
    sock.listen(1)
    print(f'Escutando em {sock.getsockname()}')
    while True:
        print("Esperando conexões")
        conn , addres = sock.accept()
        print(f'Conexao estabelecida com : {addres}')
        message =  recvall(conn, 16)
        print('Recebendo mensagem do tipo 16 octetos:', repr(message))
        conn.sendall(b'Fechado, cliente') # Envia os dados. Obs.: Atencao ao conteudo
        conn.close()
        print('  Resposta enviada, socket fechado')


servidor(1025)

    















