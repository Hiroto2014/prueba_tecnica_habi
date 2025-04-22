""" Archivo Principal de la Logica, que Levanta el entorno para correr de forma local cada API """
from http.server import HTTPServer, BaseHTTPRequestHandler
from router import handle_get_properties, handle_post_properties_likes

class RequestHandler(BaseHTTPRequestHandler):
    """Declarar Metodos GET"""
    def do_GET(self):
        handle_get_properties(self)

    """Declarar Metodos POST"""
    def do_POST(self):
        handle_post_properties_likes(self)

"""Puerto en que va a correr el servidor local e inicialización"""
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()