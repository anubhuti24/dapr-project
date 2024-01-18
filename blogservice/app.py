from fastapi import FastAPI
from dapr.clients import DaprClient
from models import Blog

app = FastAPI()

PUBSUB_NAME = 'notifypubsub'
TOPIC = 'notify'


@app.post('/blogpost')
def blogpost(payload: Blog):
    # To publish the blog
    with DaprClient() as client:
        client.publish_event(pubsub_name=PUBSUB_NAME, topic_name=TOPIC, data=(payload.model_dump_json()))

    return {"message": "Successfully posted blog."}
