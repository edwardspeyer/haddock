import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

db = sqlite3.connect(':memory:')

db.executescript('create table cats(name, color);')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'hello')

    def do_POST(self):
        self.path

HTTPServer(('0.0.0.0', 8880), Handler).serve_forever()
