import unittest

import wildhost


class TestWildhost(unittest.TestCase):
    def test_resolves_valid(self):
        assert wildhost.resolves('google.com')

    def test_resolves_invalid(self):
        assert not wildhost.resolves('xxxx.google.com')

    def test_resolves_random(self):
        assert not wildhost.resolves_random('google.com')
