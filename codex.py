import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()
path = "https://api.jdoodle.com/v1/execute"
CLIENTID = os.getenv("CLIENTID")
CLIENTSECRET = os.getenv("CLIENTSECRET")

def getScript(script: str):
    payload = {
        "script": script,
        "stdin": "",
        "language": "python3",
        "versionIndex": "0",
        "clientId": CLIENTID,
        "clientSecret": CLIENTSECRET
    }
    response = requests.post(url=path, headers = {"Content-Type" : "application/json"}, data=json.dumps(payload))
    return response.text