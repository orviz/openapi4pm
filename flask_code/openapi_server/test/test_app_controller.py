# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.ml_app import MLApp  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAppController(BaseTestCase):
    """AppController integration test stubs"""

    def test_get_ml_app_by_name(self):
        """Test case for get_ml_app_by_name

        Get ML application by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/mlapp/{appname}'.format(appname='appname_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_ml_app(self):
        """Test case for update_ml_app

        Updated app
        """
        ml_app = {
  "appname" : "PlantClassificator",
  "entrypoint" : "plant_classificator",
  "methods" : "[\"predict\",\"train\"]",
  "contact" : "jane.doe@example.com"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/mlapp/{appname}'.format(appname='appname_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(ml_app),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
