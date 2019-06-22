# project/tests/test_eval.py


import json

from project.tests.base import BaseTestCase


class TestBaseBlueprint(BaseTestCase):

    def test_pingAuth(self):
        """Ensure the /pingAuth route behaves correctly."""
        response = self.client.get(
            '/base/pingAuth',
            headers=dict(Authorization='Bearer test')
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_ping_no_header(self):
        """Ensure error is thrown if 'Authorization' header is empty."""
        response = self.client.get('/base/pingAuth')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 403)
        self.assertIn('Provide a valid auth token.', data['message'])
        self.assertIn('error', data['status'])

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get(
            '/base/ping',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_api(self):
        """Ensure the /api route behaves correctly."""
        response = self.client.get(
            '/base/api/thermalPowerGenerationCO2',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])

    def test_api_key_do_not_exist(self):
        """There is no key match what client giving."""
        response = self.client.get(
            '/base/api/thermalPowerGenerationCO1',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertIn('fail', data['status'])

    def test_api_resource_error(self):
        """Resource doesn't response."""
        response = self.client.get(
            '/base/api/error',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('fail', data['status'])

