from http.server import BaseHTTPRequestHandler, HTTPServer
from constants import *
from socket import socket, AF_INET, SOCK_DGRAM

def send_to_backend(message):
    s = socket(AF_INET, SOCK_DGRAM)
    #address = ('backend', BACKEND_PORT)
    address = ('0.0.0.0', BACKEND_PORT)
    print(f'sending {message} to backend')
    s.sendto(message.encode(), address)
    return s.recv(1024).decode()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = self.path.removeprefix('/')
        response = send_to_backend(f'GET {name}')
        assert response.startswith('CAT')
        fields = response.split("'")
        self.send_response(200)
        self.end_headers()
        color = fields[3]
        self.wfile.write(color.encode())

    def do_POST(self):
        _, name, color = self.path.split('/')
        response = send_to_backend(f'ADD {name} {color}')
        self.send_response(200)
        self.end_headers()


def start():
    address = ('0.0.0.0', FRONTEND_PORT)
    with HTTPServer(address, Handler) as s:
        print(f'{__name__} listening on {address}')
        s.serve_forever()
