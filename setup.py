from setuptools import setup, find_packages

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="midea-beautiful-dehumidifier",
    version=__version__,
    url="https://github.com/nbogojevic/midea-beautiful-dehumidifier",
    author="Nenad Bogojevic",
    author_email="nenad.bogojevic@gmail.com",
    license="MIT",
    description=(
        "A library to control Midea Dehumidifiers"
        " via the Local area network"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
    ],
    install_requires=[
        "cryptography>=3.4",
        "requests>=2.25.1",
        "ifaddr>=0.1.7",
    ],
)
