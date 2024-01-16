import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()
sample_emails = ['mysticdocker@gmail.com']


@app.get('/dapr/subscribe')
def subscribe():
    subscriptions = [{
        'pubsubname': 'notifypubsub',
        'topic': 'notify',
        'route': 'notify'
    }]
    print('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))
    return subscriptions


@app.post('/notify')
def send_email():
    print("Email send")
    return {'status': 'success'}
