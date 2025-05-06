from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    email = fields.Email(required=True)
    is_admin = fields.Bool(dump_only=True)

class UserCreateSchema(UserSchema):
    password = fields.Str(required=True, validate=validate.Length(min=8), load_only=True)

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)