from apistar import Route, Include
from apistar.handlers import docs_urls, static_urls

from views import parse_message, list_expenses, retrieve_balance, list_users, create_user, list_by_id

user_routes = [
	Route('/', 'POST', create_user),
	Route('/', 'GET', list_users),
	Route('/{user_id}', 'GET', list_by_id), 
	Route('/query', 'POST', parse_message),
    Route('/{id}/balance', 'GET', retrieve_balance),
    Route('/{id}/expenses', 'GET', list_expenses),
]

routes = [
    Include('/users', user_routes),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
