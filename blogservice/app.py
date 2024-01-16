from fastapi import FastAPI
import json
from fastapi.encoders import jsonable_encoder
from models import Blog

app = FastAPI()


@app.post('/blogpost')
async def blogpost(payload: Blog):
    # To publish the blog
    return {"message": "Successfully posted blog."}
