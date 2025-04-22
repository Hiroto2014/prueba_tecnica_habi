""""""
from urllib.parse import urlparse, parse_qs
from controller import get_filtered_properties
from utils import send_json_response

def handle_get_properties(handler):
    parsed = urlparse(handler.path)
    if parsed.path == "/get_properties":
        filters = parse_qs(parsed.query)
        if filters['state'][0] in ("comprando", "comprado"):
            send_json_response(handler,{"Error":"State Not Allowed"},400)

        response = get_filtered_properties(filters)
        send_json_response(handler, response)
    else:
        send_json_response(handler,{"Error":"Properties Not Found"},404)

def handle_post_properties_likes(handler):
    parsed = urlparse(handler.path)
    if parsed.path == "/post_likes_properties":
        filters = parse_qs(parsed.query)
    else:
        send_json_response(handler,{"Error":"Properties Not Found"},404)