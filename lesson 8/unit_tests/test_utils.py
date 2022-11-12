import unittest
import os
import sys
import argparse

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.utils import create_parser
from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT


class TestUtils(unittest.TestCase):
    test_args = None

    def setUp(self) -> None:
        test_parser = argparse.ArgumentParser()
        test_parser.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
        test_parser.add_argument('-p', '--port', default=DEFAULT_PORT, type=int)
        self.test_args = vars(test_parser.parse_args())

    def tearDown(self) -> None:
        pass

    def test_create_parser(self):
        parser = create_parser()
        args = vars(parser.parse_args())
        self.assertEqual(args, self.test_args)
