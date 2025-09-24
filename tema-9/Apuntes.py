#1 . Archivos y directorios

#En Python puedes leer, crear, modificar y borrar archivos y carpetas usando módulos de la biblioteca estándar como os, pathlib y shutil.
#Ejemplo básico:
from pathlib import Path

# Crear un archivo y escribir texto
ruta = Path("ejemplo.txt")
ruta.write_text("Hola, mundo!")

# Leer contenido
print(ruta.read_text())

# 2. Compresión
#Python permite comprimir y descomprimir archivos en formatos como .zip o .tar.
import zipfile

with zipfile.ZipFile("archivo.zip", "w") as zipf:
    zipf.write("ejemplo.txt")

#Esto es útil para ahorrar espacio o enviar datos agrupados.

# 3. Redes y flujos
#Con módulos como socket, http.client o librerías como requests, Python puede conectarse a internet, enviar/recibir datos y manejar protocolos.
#Ejemplo (cliente simple con requests):
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resp.json())
#Esto permite interactuar con APIs y servicios web.

#4. El formato de intercambio de datos JSON
#JSON es un formato muy usado para compartir información entre sistemas. Python tiene el módulo json para leer y escribirlo.
import json

data = {"nombre": "Ana", "edad": 25}
json_str = json.dumps(data)   # dict → JSON
print(json_str)

data2 = json.loads(json_str)  # JSON → dict
print(data2["nombre"])

#5. Persistencia de datos con pickle y shelve
#Sirven para guardar objetos de Python en disco y cargarlos después.
#pickle guarda estructuras en un archivo binario:
import pickle

datos = {"x": 1, "y": [1,2,3]}
with open("datos.pkl", "wb") as f:
    pickle.dump(datos, f)

#shelve funciona como una base de datos clave-valor, pero almacenando objetos Python:
import shelve

with shelve.open("mi_bd") as db:
    db["usuario"] = {"nombre": "Ana", "edad": 25}

# 6. Persistencia de datos con SQLAlchemy
#SQLAlchemy es una librería para trabajar con bases de datos relacionales (MySQL, PostgreSQL, SQLite, etc.) usando Python.
#Ejemplo con SQLite:
from sqlalchemy import create_engine, Column, Integer, String, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///ejemplo.db")
Session = sessionmaker(bind=engine)
session = Session()
# Te permite crear tablas, insertar y consultar datos de forma más ordenada y profesional.

# 7. Archivos de configuracion : Muchos programas usan archivos de configuración (ej. .ini, .yaml, .json) para guardar parámetros.
#Python tiene el módulo configparser para .ini:
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print(config["DEFAULT"]["usuario"])
