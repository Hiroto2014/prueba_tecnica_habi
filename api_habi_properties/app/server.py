from http.server import HTTPServer, BaseHTTPRequestHandler
from router import handle_get_properties, handle_post_properties_likes

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_get_properties(self)

    def do_POST(self):
        handle_post_properties_likes(self)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()