import json 
from flask import request

def heartbeat():
    response = {
        "msg": "Hello World!"
    }
    return response 

def headers():
    output = dict()
    for i in request.headers.items():
        output[i[0]] = i[1]
    return output
