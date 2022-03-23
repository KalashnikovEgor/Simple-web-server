from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    # def parse_url(self):
    #     request = self.path
    #     print(request)
    #     parsed_url = urlparse(request)
    #     dict = parse_qs(parsed_url.query)
    #     return dict


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        request = self.path
        parsed_url = urlparse(request)
        dict = parse_qs(parsed_url.query)
        if 'name' in dict and 'message' in dict:
            name = dict['name']
            message = dict['message']
            self.wfile.write(bytes("<p>Hello  %s</p>" % name[0], "utf-16"))
            self.wfile.write(bytes(message[0], "utf-16"))
        else:
            self.wfile.write(bytes("Наберите get запрос (/?name=Rekruto&message=Давай дружить!) и всё заработает <br> Надеюсь я правильно понял задание :)", "utf-16"))






if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
