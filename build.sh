#!/bin/bash
set -e

# Install dependencies
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# Build package
python setup.py sdist bdist_wheel
