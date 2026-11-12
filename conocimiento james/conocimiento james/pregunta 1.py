#1. Paquetes de más de 4 días con destino a Cartagena o a San Andrés.

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["toursystem"]

paquetes = db["paquete turistico"]

consulta = {
    "duracion": {"$gt": 4},
    "destino.ciudad": {
        "$in": ["Cartagena", "San Andres"]
    }
}

for paquete in paquetes.find(consulta):
    print(paquete)

cliente.close()
