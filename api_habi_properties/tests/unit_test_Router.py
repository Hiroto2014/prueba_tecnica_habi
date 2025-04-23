"""Archivo de pruebas Unitarias de la conección a la base, con datos Dinamicos simulando una petición correcta de cada API y su manejo de Error"""
import unittest
from unittest.mock import patch, MagicMock
from api_habi_properties.app.router import handle_get_properties

class TestHandleGetProperties(unittest.TestCase):

    """Prueba Unitaria de Respuesta Correcta del API"""
    @patch("api_habi_properties.app.router.send_json_response")
    @patch("api_habi_properties.app.router.get_filtered_properties")
    def test_handle_get_properties_valid(self, mock_get_filtered_properties, mock_send_json_response):
        # Simular handler con query string válida
        mock_handler = MagicMock()
        mock_handler.path = "/get_properties?state=pre_venta&city=Bogota"

        mock_get_filtered_properties.return_value = {"result": "ok"}

        handle_get_properties(mock_handler)

        mock_get_filtered_properties.assert_called_once()
        mock_send_json_response.assert_called_with(mock_handler, {"result": "ok"})

    """Prueba Unitaria de Respuesta con Valor de Estado no Permitido"""
    @patch("api_habi_properties.app.router.send_json_response")
    def test_handle_get_properties_internal_state_blocked(self, mock_send_json_response):
        mock_handler = MagicMock()
        mock_handler.path = "/get_properties?state=comprando"

        handle_get_properties(mock_handler)

        mock_send_json_response.assert_called_once_with(mock_handler, {"Error": "State Not Allowed"}, 400)

    """Prueba Unitaria de Respuesta con Dato que no Existe en la Base y no trae Data"""
    @patch("api_habi_properties.app.router.send_json_response")
    def test_handle_get_properties_invalid_path(self, mock_send_json_response):
        mock_handler = MagicMock()
        mock_handler.path = "/invalid_path?state=TEST"

        handle_get_properties(mock_handler)

        mock_send_json_response.assert_called_once_with(mock_handler, {"Error": "Properties Not Found"}, 404)

if __name__ == "__main__":
    unittest.main()
