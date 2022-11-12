import unittest
import os
import sys
import json

sys.path.append(os.path.join(os.getcwd(), '..'))
from client import serv_answer_parsing


class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_200_answer(self):
        self.assertEqual(serv_answer_parsing({'response': 200}), '200 OK')

    def test_400_answer(self):
        self.assertEqual(serv_answer_parsing({'response': 400}), '400 Bad Request')

    def test_other_answer(self):
        self.assertEqual(serv_answer_parsing({'response': 10}), '400 Bad Request')
