#2. Paquetes de destinos de una región específica que incluyan alojamiento.

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["toursystem"]

paquetes = db["paquete turistico"]

consulta = {
    "destino.region": "Caribe",
    "alojamiento": {
        "$exists": True,
        "$ne": None
    }
}

for paquete in paquetes.find(consulta):
    print(paquete)

cliente.close()
