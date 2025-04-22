"""Este Documento Tiene la Ruta de Cada Petición de la Logica Implementada, además de Logica Interna de cada Endpoint"""
from urllib.parse import urlparse, parse_qs
from api_habi_properties.app.controller import get_filtered_properties, get_likes_properties_data
from api_habi_properties.app.utils import send_json_response

"""Petición para Obtener las Propiedades con los filtros Enviados por el usuario"""
def handle_get_properties(handler):
    parsed = urlparse(handler.path)
    if parsed.path == "/get_properties":
        filters = parse_qs(parsed.query)
        #Condicional para evitar mostrar propiedades con Status Internos
        if filters['state'][0] in ("comprando", "comprado"):
            send_json_response(handler,{"Error":"State Not Allowed"},400)
            return #

        response = get_filtered_properties(filters)
        send_json_response(handler, response)
    else:
        send_json_response(handler,{"Error":"Properties Not Found"},404)

"""Petición para Insertar los Datos de Cada Megusta del Usuario a la Propiedad"""
def handle_post_properties_likes(handler):
    parsed = urlparse(handler.path)
    if parsed.path == "/post_likes_properties":
        filters = parse_qs(parsed.query)
        response = get_likes_properties_data(filters)
        send_json_response(handler, response)
    else:
        send_json_response(handler,{"Error":"Properties Not Found"},404)