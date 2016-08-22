__author__ = 'jacob'
import unittest


class TestStringMethods(unittest.TestCase):

    def test_abstract(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_citation(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_references(self):
        self.assertEqual(True, 1)

if __name__ == '__main__':
    unittest.main()