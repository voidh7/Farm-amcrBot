from setuptools import setup, find_package

setup(
    name="amrc farm bot",
    version="1.0.0",
    description="bot para minerar amoracoin",
    author="vøidh7",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31",
        "pyfiglet>=0.8"
    ],


