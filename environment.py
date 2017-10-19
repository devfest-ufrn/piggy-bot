from apistar import environment, typesystem


class Env(environment.Environment):
    properties = {
        'DIALOG_FLOW_ACCESS_TOKEN': typesystem.string(default=''),
        'DATABASE_URL': typesystem.string(default='sqlite:///temp.db')
    }


env = Env()