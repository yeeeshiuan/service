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

    def test_normalAPI(self):
        """Ensure the /normalAPI route behaves correctly."""
        response = self.client.post(
            '/base/normalAPI',
            data=json.dumps({
                'url': 'http://data.taipower.com.tw/opendata/apply/file/d061002/%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E5%85%AC%E5%8F%B8_%E7%81%AB%E5%8A%9B%E7%99%BC%E9%9B%BB_%E6%BA%AB%E5%AE%A4%E6%B0%A3%E9%AB%94%E6%8E%92%E6%94%BE%E9%87%8F.csv',
            }),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])

    def test_normalAPI_resource_error(self):
        """Resource doesn't response."""
        response = self.client.post(
            '/base/normalAPI',
            data=json.dumps({
                'url': 'https://www.google.com/5566',
            }),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('fail', data['status'])
