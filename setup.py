import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 8):
    sys.exit('Sorry, Python < 3.8 is not supported')

setup(
    name="browser-use",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium>=4.16.0",
        "webdriver_manager>=4.0.1",
    ],
    python_requires=">=3.8",
    package_data={
        "browser_use": [
            "i18n/*.json",
            "static/*",
        ],
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
