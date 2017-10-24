import datetime
import json
from http import HTTPStatus

import apiai
from apistar import http, Response
from sqlalchemy import func
from sqlalchemy.orm import Session

from environment import env
from models import Expense, PendingQuery, User
from schema import ExpenseSchema

ai = apiai.ApiAI(env['DIALOG_FLOW_ACCESS_TOKEN'])


def get_intent_name(dialog_flow_response):
    return dialog_flow_response['result']['metadata']['intentName']


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

    dialog_flow_response = json.loads(response.read().decode('utf-8'))
    intent = get_intent_name(dialog_flow_response)

    if intent == 'register_expense':
        expense = register_expense(session, dialog_flow_response)
        return Response({'content': 'Expense of %0.2f registered' % expense.value}, status=HTTPStatus.OK)

    return Response(dialog_flow_response['result'], status=HTTPStatus.OK)


def retrieve_balance(session: Session):
    """
    Function responsible to return the current balance of the user
    :param session:
    :return:
    """
    balance = session.query(func.sum(Expense.value)).scalar()
    return Response({'balance': balance}, status=HTTPStatus.OK)


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
    expense.value = float(response['result']['parameters']['value'])

    session.add(expense)
    session.flush()

    return expense


def list_users(session: Session, response):
    """
    Function responsible to list all the users
    :param session:
    :return:
    """
    # queryset = session.query(User).all()
    # return [UserSchema(user) for user in queryset]
    pass


def create_user(session: Session, new_user: User):

    user = User()
    user.id = new_user.id
    user.username = new_user.username
    user.first_name = new_user.first_name

    session.add(user)
    session.flush()

    return user
