import socket, select, string, sys

def prompt():
    sys.stdout.write('Eu: ')
    sys.stdout.flush

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print ("Usar: python client.py hostname port")

    host = sys.argv[1]
    port = sys.argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except:
        print("Não foi possível conectar!")
        sys.exit()
    
    print ("Conetado com o host")

    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
    #https://www.binarytides.com/code-chat-application-server-client-sockets-python/