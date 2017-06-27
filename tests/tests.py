#!/usr/bin/env python3
# author: @manojpandey

import unittest
from fbfinder.fbfinder import *

class FbFinderTests(unittest.TestCase):

    base_url = "http://facebook.com/"

    def test_invalid_url(self):
        input_url = "htt://google.com"
        result = FbFinder.find_id(input_url)
        known_result = "Invalid URL"
        self.assertEqual(result, known_result)

    def test_different_domain_url(self):
        input_url = "https://github.com"
        result = FbFinder.find_id(input_url)
        known_result = "Not a facebook URL"
        self.assertEqual(result, known_result)

    def test_invalid_url(self):
        input_url = "https://github.com/404"
        result = FbFinder.find_id(input_url)
        known_result = "Not a valid page"
        self.assertEqual(result, known_result)

    def test_good_url(self):
        input_url = "https://facebook.com/onlyrealmvp"
        result = FbFinder.find_id(input_url)
        known_result = "100001321298318"
        self.assertEqual(result, known_result)

    def test_only_handle(self):
        input_handle = "onlyrealmvp"
        build_url = self.base_url + input_handle
        result = FbFinder.find_id(build_url)
        known_result = "100001321298318"
        self.assertEqual(result, known_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
