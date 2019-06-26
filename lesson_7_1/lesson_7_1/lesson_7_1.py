import socket
import views


class WebServer:
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.websocket = ("127.0.0.1", port)
        self.urls = {
            "/":views.index(),
            "/about": "about page",
            }


    def get_headers(self, url):
        if url in self.urls:
            return "HTTP/1.1 200 OK\n\n", 200
        else:
            return "HTTP/1.1 404 not found\n\n", 404




    def get_content(self, url, code):
        if code == 200:
            return self.urls[url]
        elif code == 404:
            return "<h1> page not found </h1>"








    def parse_url(self, reqest):
        return reqest.split(" ")[1]












    def server_response(self, reqest):
        url = self.parse_url(reqest)
        headers, code = self.get_headers(url)
        content = self.get_content(url, code)
        return headers + content






    def start(self):
        self.server_socket.bind(self.websocket)
        self.server_socket.listen()
    

        while True:
            client_socket, address = self.server_socket.accept()
            reqest = client_socket.recv(2048)


            response = self.server_response(reqest.decode())



            print(address)
            print(reqest)


            client_socket.sendall(response.encode())
            client_socket.close()





WebServer(8000).start()


