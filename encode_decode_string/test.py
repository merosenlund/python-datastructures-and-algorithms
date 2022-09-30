import unittest

import code

class Test(unittest.TestCase):

    def test_encode_return_type(self):
        result = code.encode(["string1", "string2"])
        self.assertEqual(str, type(result), "Encode returns a string")


    def test_encode_works(self):
        result = code.encode(["string1", "string2"])
        self.assertEqual(result, "7#string17#string2", "Encode correctly encodes string")


    def test_decode_return_type(self):
        result = code.decode("7#string17#string2")
        self.assertEqual(list, type(result), "Decode returns a list")


    def test_decode_works(self):
        result = code.decode("7#string17#string2")
        self.assertEqual(len(result), 2, "Decode returns a list of 2 when '7#string17#string2' is passed in")


    def test_decode_is_correct(self):
        result = code.decode("7#string17#string2")
        self.assertEqual(result[0], "string1", "Decode has the correct string at element 0")
        self.assertEqual(result[1], "string2", "Decode has the correct string at element 1")


if __name__ == '__main__':
    unittest.main()