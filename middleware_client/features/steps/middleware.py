import asyncio

from behave import *
from world import host_client as host


@given('host is running')
def step_impl(context):
    context.host = host
    response = asyncio.run(context.host.get_load_check())  # ConnectionRefusedError
    assert 'currentLoad' in response

@when('asked for managers')
def step_impl(context):
    context.results = asyncio.run(context.mw.list_managers())

@when ('asked for manager {id}')
def step_impl(context, id: str):
    if id == '-':
        id = context.results[0]['id']
    context.results = asyncio.run(context.mw.get_manager_client(id))

@then('returns response with Client: {object}')
def step_impl(context, object):
    assert context.results.__class__.__name__ == object

@then('returns response with managers')
def step_impl(context):
    resp = context.results
    for manager in resp:
        assert 'id' in manager

@then('host is still running')
def step_impl(context):
    response = asyncio.run(context.host.get_load_check())  # ConnectionRefusedError
    assert 'currentLoad' in response
