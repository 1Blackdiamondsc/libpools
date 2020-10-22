import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


# exposing the params so it can be imported
setup_params = {
    "name": "pools",
    "version": "20201022",
    "description": "Python library for pools liquidity providers",
    "long_description": read("README.md"),
    "long_description_content_type": "text/markdown",
    "author": "Andre Miras",
    "url": "https://github.com/AndreMiras/libpools",
    "packages": ["pools"],
    "install_requires": [
        "cachetools",
        "gql==3.0.0a3",
        "web3",
    ],
    "extras_require": {
        "dev": [
            "black",
            "flake8",
            "isort",
            "pytest",
            "tox",
            "twine",
            "wheel",
        ]
    },
}


def run_setup():
    setup(**setup_params)


# makes sure the setup doesn't run at import time
if __name__ == "__main__":
    run_setup()
