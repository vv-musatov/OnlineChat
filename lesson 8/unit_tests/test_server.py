import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))
from server import client_answer_parsing
from common.actions import RESPONSE_200, RESPONSE_400


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_client_answer_parsing_200(self):
        self.assertEqual(client_answer_parsing({'action': 'presence'}), RESPONSE_200)

    def test_client_answer_parsing_400(self):
        self.assertEqual(client_answer_parsing({'action': 'other'}), RESPONSE_400)
