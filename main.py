from fastapi import FastAPI, status, Response
import uvicorn
from typing import Optional

app = FastAPI()

users = [
    {
        "id":1,
        "nombre": "Gustavo",
        "apellido": "Valmaña",
        "edad": 35
    },
    {
        "id":2,
        "nombre": "Janny",
        "apellido": "Hernandez",
        "edad": 33
    },
    {
        "id":3,
        "nombre": "Aihoa",
        "apellido": "Valmaña",
        "edad": 2
    },       
]

@app.get('/')
async def message():
    return "Hola mundo"

@app.get('/users', name= 'List all users')
async def get_users():
    return users

@app.get('/user/{id}',name="Get user by id")
async def get_ser(id:int, edad:int, nombre:Optional[str] = None):
    if not nombre:
        print("Nombre no enviado")
    for user in users:
        if user['id'] == int(id) and user['edad'] == int(edad) and user['nombre'] == nombre:
            return user
    return "User not found"

@app.get('/welcome/{nombre}/{apellido}')
async def welcome(nombre:str, apellido:str, response: Response):
    return f"Bienvenido {nombre} {apellido}"

@app.get('/suma/{numero1}/{numero2}')
async def sum(numero1: int, numero2:int, response: Response):
    if numero1 + numero2 > 0:
        response.status_code = status.HTTP_200_OK
        return numero1 + numero2
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000, reload=True)