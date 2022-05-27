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

### What is Swagger?

---
Swagger allows you to describe the structure of your APIs so that machines can read them. The ability of APIs to describe their own structure is the root of all awesomeness in Swagger. Why is it so great? Well, by reading your API’s structure, we can automatically build beautiful and interactive API documentation. We can also automatically generate client libraries for your API in many languages and explore other possibilities like automated testing. Swagger does this by asking your API to return a YAML or JSON that contains a detailed description of your entire API. This file is essentially a resource listing of your API which adheres to OpenAPI Specification. The specification asks you to include information like:
What are all the operations that your API supports?
What are your API’s parameters and what does it return?
Does your API need some authorization?
And even fun things like terms, contact information and license to use the API.
You can write a Swagger spec for your API manually, or have it generated automatically from annotations in your source code. Check swagger.io/open-source-integrations for a list of tools that let you generate Swagger from code.

[Source](https://swagger.io/docs/specification/2-0/what-is-swagger/)
