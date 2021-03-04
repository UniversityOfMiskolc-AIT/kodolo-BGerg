import unittest
from coder.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_encoding(self):
        self.assertEqual("65 2 1", encoding("ACD"))
        self.assertEqual("32 4 12 78", encoding(" $0~"))
        self.assertEqual("123 -2 -82", encoding("{y'"))

    def test_decoding(self):
        self.assertEqual("ACD", decoding("65 2 1"))
        self.assertEqual(" $0~", decoding("32 4 12 78"))
        self.assertEqual("{y'", decoding("123 -2 -82"))




