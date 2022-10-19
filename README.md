<h1 align="center"><strong>Scramjet Transform Hub API Client</strong></h1>

<p align="center">
    <a href="https://github.com/scramjetorg/transform-hub/blob/HEAD/LICENSE"><img src="https://img.shields.io/github/license/scramjetorg/transform-hub?color=green&style=plastic" alt="GitHub license" /></a>
    <a href="https://npmjs.org/package/@scramjet/sth"><img src="https://img.shields.io/github/v/tag/scramjetorg/transform-hub?label=version&color=blue&style=plastic" alt="STH version" /></a>
    <a href="https://github.com/scramjetorg/transform-hub"><img src="https://img.shields.io/github/stars/scramjetorg/transform-hub?color=pink&style=plastic" alt="GitHub stars" /></a>
    <a href="https://npmjs.org/package/@scramjet/sth"><img src="https://img.shields.io/npm/dt/@scramjet/sth?color=orange&style=plastic" alt="npm" /></a>
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


# Development guide

The best option to develop API clients is to create virtual environments for each of the client itself. Go to one of the clients directory, **client**, **manager_client**, **multimanager_client**, **middleware_client** and run:

````bash
# create virtual env
python3 -m venv venv

# activate
source venv/bin/activate

# install dependencies
pip install -r requirements_dev.txt
````

# BDD tests

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

