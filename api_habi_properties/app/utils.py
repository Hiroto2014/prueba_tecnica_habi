""" Archivos de Utilidades para el programa """
import json

""" Formateo de la Respuesta que recibira el Front """
def send_json_response(handler, data, status=200):
    response = json.dumps(data).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(response)))
    handler.end_headers()
    handler.wfile.write(response)