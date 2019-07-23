"""
    Author:Zhengzhihui
    Version:0.3
    Date:2019/07/21
    Description:TCP-IP client
"""
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Tom', b'Lily', b'Lucy']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


if __name__ == "__main__":
    main()
