from setuptools import setup
from setuptools import find_packages

NAME = "finddups"
DESCRIPTION = "My short description for my project"
KEYWORDS = "my keywords"
AUTHOR = "André P. Santos"
EMAIL = "andreztz@gmail.com"
URL = "https://github.com/andreztz/finddups"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.0.dev1"


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


package = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "keywords": KEYWORDS,
    "author": AUTHOR,
    "author_email": EMAIL,
    "python_requires": REQUIRES_PYTHON,
    "url": URL,
    "license": "my_license",
    "packages": find_packages(),
    "install_requires": required(),
    "entry_points": {"console_scripts": ["finddups-cli=finddups.__main__:main"]},
    "classifiers": [
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
}

setup(**package)
