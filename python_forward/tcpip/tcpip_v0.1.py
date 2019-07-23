"""
    Author:Zhengzhihui
    Version:0.1
    Date:2019/07/21
    Description:TCP-IP
"""
import socket
import ssl


def main():
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = ssl.wrap_socket(socket.socket())
    s.connect(('www.sina.com.cn', 443))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('sina.html', 'wb') as f:
        f.write(html)


if __name__ == "__main__":
    main()
