from apistar import Route, Include
from apistar.handlers import docs_urls, static_urls

from views import parse_message, list_expenses

routes = [
    Route('/query', 'GET', parse_message),
    Route('/expenses', 'GET', list_expenses),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
