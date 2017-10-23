import datetime
import json
from http import HTTPStatus

import apiai
from apistar import http, Response
from sqlalchemy.orm import Session

from environment import env
from models import Expense, PendingQuery
from schema import ExpenseSchema

ai = apiai.ApiAI(env['DIALOG_FLOW_ACCESS_TOKEN'])


def parse_message(session: Session, message: http.QueryParam):
    """
    Receives a message, sends to Dialogflow and register the message into database
    :param session: database session
    :param message: the message sent by the user
    :return: response message to user
    """
    request = ai.text_request()
    request.lang = 'pt_BR'
    request.session_id = 1
    request.query = message
    response = request.getresponse()

    if response.status == HTTPStatus.UNAUTHORIZED or not env['DIALOG_FLOW_ACCESS_TOKEN']:
        return Response({'error': 'Unathorized'}, status=HTTPStatus.UNAUTHORIZED)
    elif response.status != HTTPStatus.OK:
        pending = PendingQuery()
        pending.message = message
        pending.request_status = response.status
        pending.request_date = datetime.datetime.now()
        session.add(pending)
        return Response({'error': 'Something went wrong while trying to communicate with DialogFlow. STATUS=%s' % response.status})
    else:
        json_response = json.loads(response.read().decode('utf-8'))
        if json_response['result']['metadata']['intentName'] == 'register_expense':
            register_expense(session, json_response)

    return Response(json_response['result'], status=201)


def list_expenses(session: Session):
    """
    Function responsible to list all the expenses by current user
    :param session:
    :return:
    """
    queryset = session.query(Expense).all()
    return [ExpenseSchema(expense) for expense in queryset]


def register_expense(session: Session, response):
    """
    Function responsible to register the expense in database
    :param session:
    :param response:
    :return:
    """
    expense = Expense()
    expense.message = response['result']['resolvedQuery']
    expense.value = response['result']['parameters']['value']

    session.add(expense)
    session.flush()

