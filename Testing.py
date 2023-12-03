from Draft_Code import rearrange_name
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "lovalace, Ada"
        expected = "Ada lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()