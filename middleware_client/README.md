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

The package provides an API Middleware Client for use with Scramjet CPM.

Usage:

```python
import asyncio

url = 'http://0.0.0.0:7000/api/v1/'
host = MiddlewareClient(url)

version = asyncio.run(host.get_version())
print(version)
```

# Development usage

If you want to use development version, be sure that you installed all needed dependencies in editable mode. You can use **venv** with predefined **requirements_dev.txt** file. 

````bash
# cat requirements.txt
-e ../client
````

````python
python3 -m venv venv
source venv/bin/activate

pip install -r requirements_dev.txt
````

It will install api client from repository, instead of Python Package Index. To install released version, you can use **requirements.txt** file. 
