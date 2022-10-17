from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scramjet-middleware-client-py",
    version='0.1',
    author="Scramjet.org",
    author_email="<info@scramjet.org>",
    description='Scramjet is a simple reactive stream programming framework.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['features']),
    keywords=['python', 'streams', 'scramjet', 'api-client', 'middleware-client'],
    classifiers=[]
)