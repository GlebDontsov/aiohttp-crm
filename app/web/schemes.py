from marshmallow import Schema, fields


class OkResponseScheme(Schema):
    status = fields.Str()
    data = fields.Dict()
