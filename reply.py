import json
from flask import Flask, request
import requests
from wave import *

app = Flask(__name__)

@app.route('/slack/message', methods=['POST'])
def incoming_slack_message():
    req = request.values['payload']
    data = json.loads(req)
    value = data["actions"][0]["value"]
    url = data["response_url"]
    print(json.dumps(data, indent=4, sort_keys=True))
    print(value)
    print(url)
    if value == "yes":
        payload = {"text": "I love you too!! :heart:"}
        response = requests.post(data["response_url"], data=json.dumps(payload))
    else:
        payload = {"text": "I try to be better :disappointed:"}
        response = requests.post(data["response_url"], data=json.dumps(payload))
    return 'action successful'

if __name__ == "__main__":
    app.run(debug=True, port=3000)