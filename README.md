<h1 align="center"><strong>Scramjet Transform Hub Python API Client</strong> :snake:</h1>

<p align="center">
    <a href="https://github.com/scramjetorg/transform-hub/blob/HEAD/LICENSE"><img src="https://img.shields.io/github/license/scramjetorg/transform-hub?color=green&style=plastic" alt="GitHub license" /></a>
    <a href="https://github.com/scramjetorg/transform-hub"><img src="https://img.shields.io/github/stars/scramjetorg/transform-hub?color=pink&style=plastic" alt="GitHub stars" /></a>
    <a><img src="https://static.pepy.tech/personalized-badge/scramjet-api-client?period=total&units=none&left_color=purple&right_color=darkgreen&left_text=Downloads" alt="downloads" /></a> 
    <a href="https://scr.je/join-community-mg1"><img alt="Discord" src="https://img.shields.io/discord/925384545342201896?label=discord&style=plastic"></a>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7F7V65C43EBMW">
        <img src="https://img.shields.io/badge/Donate-PayPal-green.svg?color=yellow&style=plastic" alt="Donate" />
    </a>
</p>
<p align="center">⭐ Star us on GitHub — it motivates us a lot! 🚀 </p>
<p align="center">
    <img src="https://assets.scramjet.org/sth-logo.svg" alt="Scramjet Transform Hub Logo">
</p>

The package provides an API Clients for use with Scramjet Transform Hub.

## Table of contents

- [Introduction :wave:](#introduction)
- [Installation :clamp:](#installation)
- [Quick start :rocket:](#quick-start)
- [Requesting features](#requesting-features)
- [Reporting bugs](#reporting-bugs)
- [Contributing](#contributing)
- [Development Setup](#development-setup)
- [FAQ | Troubleshooting :collision:](#faq-troubleshooting-collision)
- [Dictionary :book:](#dictionary-book)

## Introduction

The package enables you to use Python API to manage and interact with Sequences/Instances within your Hubs. It has 3 main classes, they are: `HostClient`, `SequenceClient` and `InstanceClient.`


## Installation

Scramjet Framework is available on PyPI, You can install it with simple pip command:

```bash
pip install scramjet-api-client
```
## Quick start

Let's say I want to send my new custom Sequence to Hub SCP and check if it's running properly.

:bulb: Hint: If you want to use Hub SCP, make sure you have valid account on [Scramjet Cloud Platform](www.scramjet.org)

```python3
import asyncio
import json
from client.host_client import HostClient
from client.sequence_client import SequenceClient
from client.instance_client import InstanceClient
from client_utils.client_utils import ClientUtils


token = '<YOUR_TOKEN>'
space_id = '<YOUR_SPACE_ID>'
# middleware url
api_base ='https://api.scramjet.cloud/api/v1' 

ClientUtils.setDefaultHeaders({'Authorization': f'Bearer {token}'})

async def main():
    host = HostClient(f'{api_base}/space/{space_id}/api/v1/sth/sth-0/api/v1')

    # send sequence in .tar.gz and get it's uniqe id
    seq_id = await host.send_sequence('my_cool_sequence.tar.gz')
    seq_id = json.loads(seq_id)

    # pass previous id to Sequence Client and call start
    seq_client = SequenceClient(seq_id['id'], host)
    inst_id = await seq_client.start()
    inst_id = json.loads(inst_id)

    # creating an Instance Client for interaction with running Sequence 
    my_inst_client = InstanceClient(inst_id['id'], host)
    inst_info = await my_inst_client.get_info()
    print(inst_info)

asyncio.run(main())
```

### Let's brake down above snippet and explain the code line by line.

First I have to import necessary clients and set up some config stuff:

```python3
import asyncio
import json
from client.host_client import HostClient
from client.sequence_client import SequenceClient
from client.instance_client import InstanceClient
from client_utils.client_utils import ClientUtils


token = '<YOUR_TOKEN>'
space_id = '<YOUR_SPACE_ID>'

# middleware url
api_base ='https://api.scramjet.cloud/api/v1' 

# set up headers
ClientUtils.setDefaultHeaders({'Authorization': f'Bearer {token}'})
```
:bulb: Hint: Token and space id can be found in Your [profile](https://console.scramjet.cloud/profile)

Next I have to initialize, the host:

```python
host = HostClient(f'{api_base}/space/{space_id}/api/v1/sth/sth-0/api/v1')
```
Then send my sequence (you can find some example sequences [here](https://github.com/scramjetorg/platform-samples):

```python3
seq_id = await host.send_sequence('my_cool_sequence.tar.gz')
seq_id = json.loads(seq_id)
```

:bulb: Hint: You can compress your Sequence with simple ```si seq pack <sequence-name>``` (if you have [si CLI](https://www.npmjs.com/package/@scramjet/cli) installed)

Initialize Sequence Client and pass previous response as an first argument and call start:

```python3
seq_client = SequenceClient(seq_id['id'], host)
inst_id = await seq_client.start()
inst_id = json.loads(inst_id)
```
Our first Sequence is already running, but make sure by initializing its Instance Client, call get_info() method and print the response:
```python3
# creating an Instance Client for interaction with running Sequence 
my_inst_client = InstanceClient(inst_id['id'], host)
inst_info = await my_inst_client.get_info()
print(inst_info)
```

Use `asyncio.run()` - under the hood it handles couroutines lifecycles for you:

```python3
asyncio.run(main())
```

## Requesting Features

Anything missing? Or maybe there is something which would make using Scramjet Framework much easier or efficient? Don't hesitate to fill up a [new feature request](https://github.com/scramjetorg/api-client-python/issues/new)! We really appreciate all feedback.

## Reporting bugs

If you have found a bug, inconsistent or confusing behavior please fill up a [new bug report](https://github.com/scramjetorg/api-client-python/issues/new).

## Contributing

You can contribute to this project by giving us feedback ([reporting bugs](#reporting-bugs) and [requesting features](#requesting-features)) and also by writing code yourself!

The easiest way is to [create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of this repository and then [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) with all your changes. In most cases, you should branch from and target `main` branch.

Please refer to [Development Setup](#development-setup) section on how to setup this project.





## Development Setup

The best option to develop API clients is to create virtual environments for each of the client itself. Go to one of the clients directory, **client**, **manager_client**, **multimanager_client**, **middleware_client** and run:

````bash
# create virtual env
python3 -m venv venv

# activate
source venv/bin/activate

# install dependencies
pip install -r requirements_dev.txt
````

## BDD tests

We prepared basic BDD tests with Python Behave. You can read more about it [here](https://behave.readthedocs.io/en/stable/index.html)

For now, BDD tests are written only for **client**. To run, you need also install our STH platform. You can follow the guide from [here](https://www.npmjs.com/package/@scramjet/sth).

As you have installed STH, activate virtual env, install dependencies from **requirements_dev.txt** and run **behave** directly from **client** directory. You need also to download testing files from our refapps directory. You can just use our simple script from this repository. It will download all necessary files to **refapps** directory.


````bash
# download refapps
./download-refapps.sh
cd client/

# run bdd tests
behave
````

You should be able to see something similar

````bash
INFO:builtins:Before all executed
Feature: Python Host-Client BDD tests # features/host.feature:1

  @ci
  Scenario: List instances on host  # features/host.feature:4
    Given host is running           # features/steps/host.py:9 0.015s
    When asked for instances        # features/steps/host.py:20 0.003s
    Then host is still running      # features/steps/host.py:65 0.010s

  @ci
  Scenario: List sequences on host  # features/host.feature:10
    Given host is running           # features/steps/host.py:9 0.008s
    When asked for sequences        # features/steps/host.py:24 0.003s
    Then host is still running      # features/steps/host.py:65 0.008s

  @ci
  Scenario: Give version from host     # features/host.feature:16
    Given host is running              # features/steps/host.py:9 0.007s
    When asked for version             # features/steps/host.py:15 0.003s
    Then returns response with version # features/steps/host.py:61 0.000s
    Then host is still running         # features/steps/host.py:65 0.008s

...

INFO:builtins:After all executed
2 features passed, 0 failed, 0 skipped
7 scenarios passed, 0 failed, 0 skipped
27 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m13.243s

````

## FAQ Troubleshooting :collision:

## Dictionary :book:

- STH - Scramjet Transform Hub
- Sequence - program adapted to run in STH environment
- Instance - running Sequence
- Topics - are named buses over which Instances exchange messages
- si - Scramjet Command Line Interface
- Hub - virtual space, where Sequences can run and interact with each other
- Hub SCP - a Hub hosted by Scramjet Cloud Platform
