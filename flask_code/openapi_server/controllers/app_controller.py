import connexion
import six

from openapi_server.models.ml_app import MLApp  # noqa: E501
from openapi_server import util


def get_ml_app_by_name(appname):  # noqa: E501
    """Get ML application by name

    Some description of the operation.  You can use &#x60;markdown&#x60; here.  # noqa: E501

    :param appname: The name that needs to be fetched
    :type appname: str

    :rtype: MLApp
    """
    return 'do some magic!'


def update_ml_app(appname, ml_app):  # noqa: E501
    """Updated app

    Update ML application by name. # noqa: E501

    :param appname: The name that needs to be updated
    :type appname: str
    :param ml_app: Updated user object
    :type ml_app: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ml_app = MLApp.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
