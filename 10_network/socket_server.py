import socketserver
from server import HOSTNAME, PORT


class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        print(f'connection received: {self.client_address}')
        data = self.rfile.readline().strip()
        print(f'data received: {data.decode()}')
        self.wfile.write(data.upper())


if __name__ == "__main__":

    with socketserver.TCPServer((HOSTNAME, PORT), MyTCPHandler) as server:
        server.serve_forever()
