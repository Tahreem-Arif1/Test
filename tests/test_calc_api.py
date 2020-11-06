from tests import helpers
import unittest
from scripts.task2 import app


class TestCalcApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_calc(self):
        response = self.app.get('/calc')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_post_calc(self):
        calc_params = dict(op1=5, op2=7, op="+")
        response_code, json_response = helpers.make_post_request(
           app_instance=self.app, url='/calc', data=calc_params
        )
        result = json_response['result']
        self.assertEqual(response_code, 200)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main(argv=['-v'], verbosity=2)
