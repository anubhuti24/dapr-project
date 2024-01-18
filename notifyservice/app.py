from fastapi import FastAPI, Body
from dapr.ext.fastapi import DaprApp

sample_emails = ['sample1@gmail.com', 'sample2@gmail.com', 'sample3@gmail.com']

app = FastAPI()
dapr_app = DaprApp(app)


@dapr_app.subscribe(pubsub='notifypubsub', topic='notify')
def send_email(event_data=Body()):
    print("Event data: ", event_data)
    for i in sample_emails:
        print("Email send", i)
