from apistar import typesystem


class ExpenseSchema(typesystem.Object):
    properties = {
        'id': typesystem.String,
        'message': typesystem.String,
        'value': typesystem.Number,
        'user_id': typesystem.Number
    }

class UserSchema(typesystem.Object):	
	properties = {
		'id': typesystem.Integer,
		'username':typesystem.String,
		'first_name': typesystem.String
	}	