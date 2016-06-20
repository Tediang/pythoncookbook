import argparse
import errno
import os
import socket


SERVER_ADDRESS = 'localhost', 7777
REQUEST = b"""\
GET /hello HTTP/1.1
Host: localhost:7777


"""

def main(max_clients, max_conns):
    socks = []
    for client_num in range(max_clients):
        pid = os.fork()
        if pid == 0:
            for connction_num in range(max_conns):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(SERVER_ADDRESS)
                sock.sendall(REQUEST)
                socks.append(sock)
                print(connction_num)
                os._exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test client for LSBAWS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--max-conns',
        type=int,
        default=1024,
        help='Max connection'
    )
    parser.add_argument(
        '--max-clients',
        type=int,
        default=1,
        help='Max client'
    )

    args = parser.parse_args()
    main(args.max_clients, args.max_conns)