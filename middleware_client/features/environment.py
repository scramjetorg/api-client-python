import logging
import os
import signal
import subprocess
import sys

from steps.world import api_url

from middleware_client.middleware_client import MiddlewareClient

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def before_scenario(context, scenario):
    if 'localhost' in api_url and "prod" in scenario.effective_tags:
        scenario.skip("Skipping due to production-only.")

def before_all(context):
    log.info('Before all executed')
    path = '../../'

    global process
    process = subprocess.Popen(['npx', '@scramjet/sth', '--runtime-adapter=process'], cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setpgrp)
    context.mw: MiddlewareClient = MiddlewareClient(api_url)

    while True:
        output = process.stdout.readline()
        if b'Host started' in output:
            break


def after_all(context):
    log.info('After all executed')
    global process
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
