#4. Paquetes que no tienen guía asignado.

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["toursystem"]

paquetes = db["paquete turistico"]

consulta = {
    "$or": [
        {"guia": None},
        {"guia": {"$exists": False}},
        {"guia": ""}
    ]
}

for paquete in paquetes.find(consulta):
    print(paquete)

cliente.close()
