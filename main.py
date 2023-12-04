from fastapi import FastAPI
import uvicorn

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

@app.get('/users')
async def get_users():
    return users

@app.get('/user/{id}/{edad}')
async def get_ser(id:int, edad:int):
    for user in users:
        if user['id'] == int(id) and user['edad'] == int(edad):
            return user
    return "User not found"

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000, reload=True)