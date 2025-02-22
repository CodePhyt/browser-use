from setuptools import setup, find_packages

setup(
    name="browser-use",
    version="0.1.1",  # Incrementing version for new release
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium>=4.16.0",
        "webdriver_manager>=4.0.1",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "httpx>=0.27.0",
    ],
    python_requires="~=3.8",
    package_data={
        "browser_use": [
            "i18n/*.json",
            "static/*",
        ],
    },
    zip_safe=False,
    description="A Python package for browser automation and web interaction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="CodePhyt",
    author_email="codephyt@gmail.com",
    url="https://github.com/CodePhyt/browser-use",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
)
