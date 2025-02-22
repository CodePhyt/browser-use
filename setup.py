from setuptools import setup, find_packages

setup(
    name="browser-use",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium>=4.16.0",
        "webdriver_manager>=4.0.1",
    ],
    python_requires="~=3.8",
    package_data={
        "browser_use": [
            "i18n/*.json",
            "static/*",
        ],
    },
    zip_safe=False,
)
