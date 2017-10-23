from apistar import typesystem


class ExpenseSchema(typesystem.Object):
    properties = {
        'id': typesystem.String,
        'message': typesystem.String,
        'value': typesystem.Number,
    }
