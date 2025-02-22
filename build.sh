#!/bin/bash
set -e

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Upgrading pip, setuptools, and wheel..."
python -m pip install --upgrade pip setuptools wheel

echo "Installing requirements..."
pip install -r requirements.txt

echo "Building package..."
python setup.py sdist bdist_wheel

echo "Build completed successfully!"
