from pymongo.mongo_client import MongoClient #se importa MongoClient desde pymongo

#CONEXIÓN
def conexion(): #se define la conexion
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority" #se pone la conexio desde el mongo
    # Create a new client and connect to the server
    return MongoClient(uri) #se conecta el mongo client con la base de datos del servidor

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): #se define la lectura de datos 
    client = conexion() #se define client como la conexion anterior
    db = client.actividad4.data_real #se accede a la base de datos
    data_list = [] #se guarda el data_list en una lista
    for data_real_bd in db.find(): #se crea un bucle donde se  itera a través de los resultados de una consulta a una base de datos, donde cada resultado se almacena en la variable 
        data_list.append(data_real_bd) #los contenidos de la variable data_real_bd se guardan al final de la lista data_list
    return data_list #se regresa el resultado del data list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""