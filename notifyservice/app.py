import json, logging
from fastapi import FastAPI


app = FastAPI()
sample_emails = ['sample1@gmail.com', 'sample2@gmail.com', 'sample3@gmail.com']
logging.basicConfig(level=logging.INFO)


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
async def send_email():
    print("Here")
    for i in sample_emails:
        print("Email send", i)

    logging.info('Subscriber received the post')