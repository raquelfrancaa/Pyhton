# app_pymongo.py

from pymongo import MongoClient

client = MongoClient("sua_url_mongodb_atlas")
db = client['bank']  # Criar banco de dados 'bank'
collection = db['clientes']  # Criar a coleção 'clientes'

cliente = {
    "nome": "João Silva",
    "idade": 35,
    "contas": [
        {"tipo": "Corrente", "saldo": 1000.0},
        {"tipo": "Poupança", "saldo": 5000.0}
    ]
}

collection.insert_one(cliente)

cliente_inserido = collection.find_one({"nome": "João Silva"})
print(cliente_inserido)
