import unittest

from prefixeddict import PrefixedDict


class TestPrefixedDict(unittest.TestCase):
    def setUp(self):
        self.filled_dictionary = {'age': 30, 'name': 'john'}

    def test_dictionary_same_object(self):
        """
        Make sure whatever dictionary is passed to PrefixedDict is not a
        copy of it, but a reference to the very same object.
        """

        dictionary = {}
        prefixed = PrefixedDict('prefix', dictionary)

        self.assertEqual(id(dictionary), id(prefixed.dictionary))

    def test_prefixing(self):
        dictionary = {}
        prefixed = PrefixedDict('prefix-1', dictionary)
        prefixed['key'] = 'value'

        self.assertEqual(prefixed['key'], 'value')
        self.assertEqual(dictionary['prefix-1-key'], 'value')

    def test_keys(self):
        """Keys should only be prefixed internally."""

        prefixed = PrefixedDict('prefix', self.filled_dictionary)

        self.assertEqual(set(prefixed.keys()),
                         set(self.filled_dictionary.keys()))

    def test_values(self):
        prefixed = PrefixedDict('prefix', self.filled_dictionary)

        self.assertEqual(set(prefixed.values()),
                         set(self.filled_dictionary.values()))

    def test_items(self):
        prefixed = PrefixedDict('prefix', self.filled_dictionary)

        self.assertEqual(set(prefixed.items()),
                         set(self.filled_dictionary.items()))

    def test_keyerror(self):
        prefixed = PrefixedDict('prefix', {})

        with self.assertRaises(KeyError):
            prefixed['invalid-key']
