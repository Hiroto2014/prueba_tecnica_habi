# Prueba Tecnica Habi

## Tecnologias a Usar:
Python 3.10+
MySQL   
Unittest  


## Explicación Diagrama de Entidad Relación

Para implementar la funcionalidad de "me gusta" en el sistema, es necesario introducir las entidades, esto debido
a que se debe hacer una relación directa con los usuarios (los cuales ya estaran registrados y logueados al momento 
de hacer uso de esta funcionalidad) con cada propiedad a la que se le dio "me gusta", esto para tener una trazabilidad
completa, la tabla de "likes_properties" actua como una tabla intermedia, permitiendo que los usuarios puedan hacer
n veces uso de la función del "me gusta" y las propiedades pueden tambien ser resaltadas por varios usuarios.
Finalmente, se añadio el campo del "date_create", con el fin de tener un valor que sirva como punto de control de tiempo
para realizar metricas o mediciones para analisis futuros.
