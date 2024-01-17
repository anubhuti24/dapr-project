import json, logging
from fastapi import FastAPI, Body
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app)

sample_emails = ['sample1@gmail.com', 'sample2@gmail.com', 'sample3@gmail.com']
logging.basicConfig(level=logging.INFO)


@dapr_app.subscribe(pubsub='notifypubsub', topic='notify')
def send_email(event_data=Body()):
    print(event_data)
    for i in sample_emails:
        print("Email send", i)
    logging.info('Subscriber received the post')