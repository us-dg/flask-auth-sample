from flask import request
from schemas.users import UserSchema
from loader import database

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

def custom_response():
    data = {
        "Id" : 123,
        "name" : "Jonathan Sidwell",
        "email" : "Jonathan@qunatico.com",
        "platform" : "Discord",
        "bio" : "Best Quant on Planet Earth",
        "age" : 28
    }
    customer_id = request.headers.get("X-Consumer-Custom-Id")
    filtered_data = {key: (value if key in database[str(customer_id)] else "Not Authorized") for key, value in data.items()  }
    schema = UserSchema()
    # response = schema.loads(filtered_data)
    return schema.dump(filtered_data)
    
