from constants import *
import database
import socketserver


class Handler(socketserver.DatagramRequestHandler):
    def handle(self):
        try:
            command = self.rfile.readline().decode().strip()
            response = execute(command)
            self.wfile.write(response.encode())
        except Exception as ex:
            message = str(ex)[:200]
            self.wfile.write(message.encode())


def execute(command):
    print(f'COMMAND = {command}')
    verb, *args = command.split()

    if verb == 'ADD':
        assert len(args) == 2
        name, color = args
        database.add_cat(name, color)
        return 'OK'

    if verb == 'GET':
        assert len(args) == 1
        name, = args
        cat = database.get_by_name(name)
        return f'CAT {cat}'

    raise Exception(f'unparseable command: {command}')


def start():
    address = ('0.0.0.0', BACKEND_PORT)
    with socketserver.UDPServer(address, Handler) as s:
        print(f'{__name__} listening on {address}')
        s.serve_forever()
