"""Este archivo almacenara tanto las peticiones para la conección a la Base de Datos como Cada Query Necesaria para la Logica a Implementar"""
import mysql.connector

"""Credenciales de la Base de Datos"""
def get_connection():
    return mysql.connector.connect(
        host="18.221.137.98",
        port="3309",
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db"
    )

"""Función para darle Dinamismo a las peticiones de los Filtros"""
def get_and_or_where(params = None):
    if params:
        return "AND "
    else:
        return "WHERE "

"""Funcióin para Obtener los Datos de las Propiedades aplicando los respectivos Filtros"""
def query_properties(year = None, city = None, status = None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        WITH max_status_history as (
	SELECT sh.id, MAX(sh.update_date) as last_update_date, sh.property_id, sh.status_id FROM status_history sh
	GROUP BY sh.property_id
            )
        SELECT 
	        p.address, p.city, s.name, p.price, p.description FROM property p
	        JOIN max_status_history msh ON msh.property_id = p.id
	        JOIN status s ON s.id = msh.status_id
    """
    params = {}

    # Evaluar si existe cada filtro en la petición y añadirlo a la consulta base
    if year:
        filter_type = get_and_or_where(params)
        sql += filter_type + "p.year = %(year)s "
        params["year"] = year
    if city:
        filter_type = get_and_or_where(params)
        sql += filter_type + "LOWER(p.city) = LOWER(%(city)s) "
        params["city"] = city
    if status:
        filter_type = get_and_or_where(params)
        sql += filter_type + "LOWER(s.name) = LOWER(%(status)s) "
        params["status"] = status
    
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

""" Petición para Insertar los Datos en la Tabla (hipotetica) de los Megustas de la Propiedad."""
def query_likes_property(property_id, user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        INSERT INTO likes_properties (property_id, user_id, date_create)
        VALUES (%(property_id)s, %(user_id)s, NOW())
    """

    params = {}
    params["property_id"] = property_id
    params["user_id"] = user_id

    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

#if __name__ ==  "__main__":
 #   test_query = query_properties(12, "Bogota")