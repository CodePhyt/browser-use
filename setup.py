from setuptools import setup, find_packages

setup(
    name="browser-use",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium>=4.16.0",
        "webdriver_manager>=4.0.1",
        "pytest>=7.4.3",
        "black>=23.12.1",
        "flake8>=6.1.0",
        "isort>=5.13.2",
        "mypy>=1.7.1",
        "pytest-cov>=4.1.0",
        "pytest-mock>=3.12.0",
    ],
    python_requires=">=3.9",
    package_data={
        "browser_use": [
            "i18n/*.json",
            "static/*",
        ],
    },
)
