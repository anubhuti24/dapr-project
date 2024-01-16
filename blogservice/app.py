from fastapi import FastAPI
import json

app = FastAPI()


@app.post('/blogpost')
async def blogpost(payload: json):
    print(payload)
    data = json.dumps(payload)
    print('Blog posted : ' + json.dumps(data), flush=True)
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}
