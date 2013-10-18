from pymongo import MongoClient

con = MongoClient('mongodb://localhost:27017') # Se crea la conexion con la base de datos de mongo, en este caso se usa la url

db = con.tienda_virtual # El nombre de nuestra base de datos.

coleccion = db.productos # El nombre que tendra nuestra colección

producto = {
    "Nombre": "Agua Mineral",
    "Codigo de Barras": "0987654321",
    "Precio": 12.0,
    "Categoria": ["Bebidas","Basicos"],
    "Activo": True
} # En formato json agregamos los datos a nuestra base de datos.

productos = db.productos # Elegimos el documento con el que vamos a estar trabajando.

producto_id = productos.insert(producto) # Insertamos los datos a nuestra base de datos.

p = productos.find_one() # Hacemos una consulta para ver los datos que insertamos anteriomente.


for l in p:
    print l



