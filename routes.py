from apistar import Route, Include
from apistar.handlers import docs_urls, static_urls

from views import parse_message, list_gastos

routes = [
    Route('/', 'GET', parse_message),
    Route('/gastos', 'GET', list_gastos),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
