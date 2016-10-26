import unittest

from prefixeddict import PrefixedDict


class TestPrefixedDict(unittest.TestCase):
    def setUp(self):
        self.filled_dictionary = {'age': 30, 'name': 'john'}

    def test_dictionary_is_copied(self):
        """
        Make sure whatever dictionary is passed to PrefixedDict is actually
        copied, so as not to change the original one.

        This is to avoid nasty bugs which may crawl into people's code due to
        unnoticed side effects, such as modifying the original dictionary that
        was passed as parameter to PrefixedDict.
        """

        dictionary = {}
        prefixed = PrefixedDict('prefix', dictionary)

        self.assertNotEqual(id(dictionary), id(prefixed.dictionary))

    def test_default_dictionary(self):
        """
        By default, the dictionary should be a new, empty dictionary. It
        must never be the same one that was used before.
        """

        a = PrefixedDict('prefix')
        b = PrefixedDict('prefix')

        self.assertNotEqual(id(a.dictionary), id(b.dictionary))
        self.assertEqual(a.dictionary, {})
        self.assertEqual(b.dictionary, {})

    def test_prefixing_new_dict(self):
        dictionary = {}
        prefixed = PrefixedDict('prefix-1', dictionary)
        prefixed['key'] = 'value'

        self.assertEqual(prefixed['key'], 'value')
        self.assertEqual(prefixed.dictionary['prefix-1-key'], 'value')

    def test_prefixing_existing_dict(self):
        prefixed = PrefixedDict('prefix', self.filled_dictionary)

        self.assertEqual(set(prefixed.dictionary.keys()),
                         set(['prefix-age', 'prefix-name']))
        self.assertEqual(prefixed['age'], 30)
        self.assertEqual(prefixed['name'], 'john')

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
