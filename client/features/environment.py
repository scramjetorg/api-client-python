import os
import subprocess
import signal
import logging
import sys


log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def before_all(context):
    log.info('Before all executed')
    path = '../../'
    global process
    process = subprocess.Popen(['npx', '@scramjet/sth', '--runtime-adapter=process'], cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setpgrp)
    while True:
        output = process.stdout.readline()
        if b'Host started' in output:
            break


def after_all(context):
    log.info('After all executed')
    global process
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
