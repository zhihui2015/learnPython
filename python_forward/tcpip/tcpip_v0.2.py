"""
    Author:Zhengzhihui
    Version:0.2
    Date:2019/07/21
    Description:TCP-IP server
"""
import socket, threading, time


def tcplink(sock, addr):
    print("accept new connection from ", addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("connection from {} closed".format(addr))


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print("waiting for connection...")

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == "__main__":
    main()
