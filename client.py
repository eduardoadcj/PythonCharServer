# -*- coding: utf-8 -*-
import socket, select, string, sys

def prompt():
    sys.stdout.write('Eu: ')
    sys.stdout.flush

if __name__ == "__main__":

    if(len(sys.argv) < 3):
        print ("Usar: python client.py hostname port")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except Exception as e:
        print("Não foi possível conectar! "+str(e))
        sys.exit()
    
    print("Conetado com o host")

    prompt()

    while 1:

        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ('\nDesconectado do servidor')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    prompt()
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()

    #https://www.binarytides.com/code-chat-application-server-client-sockets-python/