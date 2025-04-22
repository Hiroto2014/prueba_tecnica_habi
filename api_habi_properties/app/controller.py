""" Este Documento Almacenara la sección donde se separan los datos de la Petición"""
from api_habi_properties.app.db import query_properties, query_likes_property

"""Se separan los componentes del filtro (Años, Ciudad, Estado) de la petición"""
def get_filtered_properties(filters):
    year = filters.get("year", [None])[0]
    city = filters.get("city", [None])[0]
    state = filters.get("state", [None])[0]

    return query_properties(year, city, state)

"""Se separan los componentes de los datos de la petición (Id Propiedad, Id Usuario) de la petición"""
def get_likes_properties_data(filters):
    property_id = filters.get("property_id", [None])(0)
    user_id = filters.get("user_id", [None])(0)

    return query_likes_property(property_id, user_id)