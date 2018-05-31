from setuptools import setup

setup(
    name="UrlShortener",
    version="1.0",
    author="Eury Pérez",
    classifiers=[
         "Development Status :: 1 - Planning"
    ],
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "SQLAlchemy",
        "Flask-Cache",
        "uWSGI",
        "passlib",
        "Flask-Sslify",
        "PyCrypto",
        "Flower",
        "SimpleJson"
    ]
)
