import unittest

import wildhost


class TestWildhost(unittest.TestCase):
    def test_resolves_valid(self):
        assert wildhost.resolves('google.com')
