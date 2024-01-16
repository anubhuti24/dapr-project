from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def blogpost():
    return "Hello World"
