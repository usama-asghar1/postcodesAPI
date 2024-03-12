import unittest
from postcode_class import *
from payload_class import *


class StatusCodeTest(unittest.TestCase):
    def test_status_check(self):
        actual_result = GETPostcodeParser("se288at").status
        expected_result = 200
        self.assertEqual(expected_result, actual_result)
