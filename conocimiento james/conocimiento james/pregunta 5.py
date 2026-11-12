#5. Los 5 paquetes más económicos por persona, mostrando solo nombre, destino y precio.

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["toursystem"]

paquetes = db["paquete turistico"]

consulta = paquetes.find(
    {},
    {
        "_id": 0,
        "nombre": 1,
        "destino": 1,
        "precio": 1
    }
).sort("precio", 1).limit(5)

for paquete in consulta:
    print(paquete)

cliente.close()
