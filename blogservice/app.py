from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from models import Blog
import logging, requests, time

app = FastAPI()

logging.basicConfig(level=logging.INFO)
base_url = 'http://127.0.0.1:3502'
PUBSUB_NAME = 'notifypubsub'
TOPIC = 'notify'
logging.info('Publishing to baseURL: %s, Pubsub Name: %s, Topic: %s' % (
    base_url, PUBSUB_NAME, TOPIC))


@app.post('/blogpost')
def blogpost(payload: Blog):
    # To publish the blog
    requests.post(
        url='%s/v1.0/publish/%s/%s' % (base_url, PUBSUB_NAME, TOPIC),
        json=jsonable_encoder(payload)
    )

    time.sleep(1)
    return {"message": "Successfully posted blog."}
