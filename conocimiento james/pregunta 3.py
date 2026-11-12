#3. Paquetes con alguna actividad de aventura que dure más de 3 horas (misma actividad).

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["toursystem"]

paquetes = db["paquete turistico"]

consulta = {
    "actividades": {
        "$elemMatch": {
            "tipo": "aventura",
            "duracion": {"$gt": 3}
        }
    }
}

for paquete in paquetes.find(consulta):
    print(paquete)

cliente.close()
