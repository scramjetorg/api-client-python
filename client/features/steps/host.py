import asyncio

from behave import *
from world import host_client as host

from client.instance_client import InstanceClient
from client.sequence_client import SequenceClient


@given('host is running')
def step_impl(context):
    context.host = host
    response = asyncio.run(context.host.get_load_check())  # ConnectionRefusedError
    assert 'currentLoad' in response

@when('asked for version')
def step_impl(context):
    context.results = asyncio.run(context.host.get_version())

@when('asked for instances')
def step_impl(context):
    context.results = asyncio.run(host.list_instances())

@when('asked for sequences')
def step_impl(context):
    context.results = asyncio.run(host.list_sequences())

@when('sequence {path} loaded')
def step_impl(context, path):
    file = asyncio.run(host.load_sequence(path))
    context.results = asyncio.run(host.send_sequence(file))

@when('{seq_id} sequence deleted')
def step_impl(context, seq_id):
    if seq_id == '-':
        seq_id = context.results.id
    context.results = asyncio.run(host.delete_sequence(seq_id))

@when('{seq_id} sequence get info')
def step_impl(context, seq_id):
    if seq_id == '-':
        seq_id = context.results.id
    context.results = asyncio.run(host.get_sequence_info(seq_id))
    assert 'id' in context.results

@when('sequence started')
def step_impl(context):
    seq: SequenceClient = context.results
    context.results = asyncio.run(seq.start())

@when('{seq_id} sequence input {input}')
def step_impl(context, seq_id, input):
    if seq_id == '-':
        inst: InstanceClient = context.results
    else:
        # else seq_id is Instance's id
        inst = InstanceClient(seq_id, host)
    assert 'instance_url' in inst.__repr__()
    context.results = asyncio.run(inst.send_input(input))

@then('is showing {instances}')
def step_impl(context, instances: str):
    assert(context.results == instances)

@then('returns response with {key} == {value}')
def step_impl(context, key: str, value: str):
    assert(context.results.get(key) == value)

@then('returns response with Client: {object}')
def step_impl(context, object):
    assert context.results.__class__.__name__ == object

@then('returns response with {key}')
def step_impl(context, key: str):
    assert(key in context.results)

@then('returns instance object')
def step_impl(context, key: str):
    assert(key in context.results)

@then('host is still running')
def step_impl(context):
    response = asyncio.run(context.host.get_load_check())  # ConnectionRefusedError
    assert 'currentLoad' in response
