from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

HOST = "0.0.0.0"
PORT = 8080

server = HTTPServer((HOST, PORT), MyHandler)
print(f"Serving on http://{HOST}:{PORT}")
server.serve_forever()
