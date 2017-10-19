from routes import routes
from apistar.backends.sqlalchemy_backend import commands, components
from apistar.frameworks.wsgi import WSGIApp as App

from environment import env
from models import Base

settings = {
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata
    },
}

app = App(routes=routes, settings=settings, commands=commands, components=components)

if __name__ == '__main__':
    app.main()
