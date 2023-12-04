from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def message():
    return "Hola mundo"

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000)