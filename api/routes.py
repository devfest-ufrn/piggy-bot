from apistar import Route, Include
from apistar.handlers import docs_urls, static_urls

from views import parse_message, list_expenses, retrieve_balance

routes = [
    Route('/query', 'GET', parse_message),
    Route('/expenses', 'GET', list_expenses),
    Route('/balance', 'GET', retrieve_balance),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
