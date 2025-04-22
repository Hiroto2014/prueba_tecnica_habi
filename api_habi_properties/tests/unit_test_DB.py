import unittest
from unittest.mock import patch, MagicMock
from api_habi_properties.app.db import get_and_or_where, query_properties

class TestQueryFunctions(unittest.TestCase):

    def test_get_and_or_where_with_params(self):
        self.assertEqual(get_and_or_where({"key": "value"}), "AND ")

    def test_get_and_or_where_without_params(self):
        self.assertEqual(get_and_or_where(), "WHERE ")
        self.assertEqual(get_and_or_where(None), "WHERE ")

    @patch("api_habi_properties.app.db.get_connection")
    def test_query_properties_no_filters(self, mock_get_connection):
        # Mocks
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{"address": "123 Main St", "city": "Bogotá", "name": "pre_venta", "price": 1000000, "description": "Hermosa casa"}]
        mock_conn.cursor.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        result = query_properties()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["city"], "Bogotá")

        mock_cursor.execute.assert_called_once()
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("api_habi_properties.app.db.get_connection")
    def test_query_properties_with_filters(self, mock_get_connection):
        # Mocks
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{"address": "calle 95 # 78 - 49","city": "bogota","name": "pre_venta","price": 120000000,"description": "hermoso acabado, listo para estrenar"}]
        mock_conn.cursor.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn

        result = query_properties(city="BOGOTA", status="pre_venta")
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "pre_venta")

        self.assertTrue(mock_cursor.execute.called)
        self.assertTrue(mock_cursor.fetchall.called)
        self.assertTrue(mock_conn.close.called)

if __name__ == "__main__":
    unittest.main()

