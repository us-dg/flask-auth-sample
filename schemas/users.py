from marshmallow import Schema,fields, EXCLUDE

class UserSchema(Schema):
  class Meta:
    unknown = EXCLUDE
  
  Id = fields.Str()
  name = fields.Str()
  email = fields.Str()
  platform = fields.Str()
  bio = fields.Str()
  age = fields.Str()