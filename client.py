import socket


class Client(object):
    def __init__(self):
        self.sock = None

    def connect(self) -> object:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 12397))
        return self.sock.recv(1024)

    def close(self) -> object:
        self.sock.close()


if __name__ == '__main__':
    try:
        while True:
            sk = Client()
            received = sk.connect()
            print(received.decode('ascii'))
    except KeyboardInterrupt:
        pass
    finally:
        sk.close()
        print("Socket Closed")
