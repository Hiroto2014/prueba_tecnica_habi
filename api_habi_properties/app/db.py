import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="18.221.137.98",
        port="3309",
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db"
    )


def get_and_or_where(params = None):
    if params:
        return "AND "
    else:
        return "WHERE "


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

    #print(params)
    #print(sql)
    
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

def query_likes_property(year = None, city = None, status = None):
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

    #print(params)
    #print(sql)

    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ ==  "__main__":
    test_dt = get_connection()
    test_query = query_properties(status="Test", city= "Bogota")