# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Example.com",
    author_email="contact@example.com",
    url="",
    keywords=["OpenAPI", "Example.com"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is an **example** API for the PredictaaS web service. # Introduction This API specification is intended to provide a skeleton for the required API paths expected for the  PredictaaS ML web service. It is OpenAPI v3 compliant, check out  [OpenAPI format](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md) for additional features. 
    """
)

