import os
import subprocess
import time
import signal
import logging
import sys

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def before_all(context):
   log.info('Before all executed')
   path = '../../'
   global process
   process = subprocess.Popen(["sth", "--runtime-adapter=process"], cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setpgrp)
   # Sleep for 10 seconds to be sure STH is up and running
   time.sleep(10)

def after_all(context):
   log.info('After all executed')
   global process
   os.killpg(os.getpgid(process.pid), signal.SIGTERM)
