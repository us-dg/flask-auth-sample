# flask-swagger-boilerplate

This is a boilerplate code for Flask API integrated with Swagger UI.
It also uses MarshMallow to structure the schemas, validate and format responses.
Projects can be created on top of this boilerplate.

## Folder Structure

api     -- stores all the main api files  
schemas -- stores the marshmallow schemas  
static  -- stores swagger config and other static files  
venv    -- stores the environment config

### What is Marshmallow? 
---
marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
In short, marshmallow schemas can be used to:

Validate input data.

Deserialize input data to app-level objects.

Serialize app-level objects to primitive Python types. The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.
