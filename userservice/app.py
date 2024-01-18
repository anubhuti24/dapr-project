from dapr.clients import DaprClient
import json

payload = {
    "title": "Dapr",
    "userid": 5,
    "content": "This is the dapr introduction."
}

with DaprClient() as d:
    resp = d.invoke_method('blog-processor', 'blogpost', data=json.dumps(payload), http_verb='post')

print('user', resp.text())