#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must install Twine:
#   $ pip install -r requirements.txt

import io
import os

from setuptools import setup

# Package meta-data.
HERE = os.path.abspath(os.path.dirname(__file__))
NAME = 'semigroups4planning'
EMAIL = '17ap87@queensu.ca'
AUTHOR = 'Alice Petrov'
REQUIRES_PYTHON = '>= 3.9 .0'
VERSION = None
LICENSE = 'MIT'
REQUIRED = [
    'macq', 'numpy', 'networkx', 'jinja2', 'pydot', 'requests', 'tarski'
]


version_ns = {}
with open(os.path.join(HERE, 'semigroups4planning', '__version__.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name="semigroups4planning",
    packages=["semigroups4planning"],
    entry_points={
        'console_scripts': ['semigroups4planning=cli:main'],
    },
    version=version_ns['__version__'],
    author=NAME,
    author_email=EMAIL,
    install_requires=REQUIRED,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ]
)