from apistar import typesystem


class GastoType(typesystem.Object):
    properties = {
        'id': typesystem.String,
        'texto': typesystem.String,
        'valor': typesystem.Number,
    }
