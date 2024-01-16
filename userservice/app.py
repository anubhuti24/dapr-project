import json
import time
import logging
import requests

logging.basicConfig(level=logging.INFO)

base_url = 'http://127.0.0.1:3500'

headers = {'dapr-app-id': 'blog-processor','content-type': 'application/json'}

payload = {
        "title": "Dapr",
        "userid": 5,
        "content": "This is the dapr introduction."
}

result = requests.post(
    url='%s/blogpost' % base_url,
    data=json.dumps(payload),
    headers=headers
)
print(result)
# print('Blog: ' + json.dumps(payload), flush=True)

time.sleep(1)
