from http.server import HTTPServer, CGIHTTPRequestHandler
print("WebOnix v0.18 (c) 2022, HappyAnd_13")
server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
