from db import query_properties, query_likes_property

def get_filtered_properties(filters):
    year = filters.get("year", [None])[0]
    city = filters.get("city", [None])[0]
    state = filters.get("state", [None])[0]

    return query_properties(year, city, state)

def get_filtered_likes_properties(filters):
    property = filters.get("property", [None])(0)
    return query_likes_property(property)