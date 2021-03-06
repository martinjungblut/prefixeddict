import unittest

from prefixeddict import PrefixedDict


class TestPrefixedDict(unittest.TestCase):
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
        prefixed = PrefixedDict('prefix', dictionary)
        prefixed['key'] = 'value'

        self.assertEqual(prefixed['key'], 'value')
        self.assertEqual(dictionary['prefix-key'], 'value')

    def test_prefix_attr(self):
        """
        Ensure the prefix's suffix(the hyphen) isn't added to the
        attribute itself when __init__ is called.
        """

        prefixed = PrefixedDict('prefix', {})
        self.assertEqual(prefixed.prefix, 'prefix')

    def test_keys(self):
        dictionary = {'age': 30, 'name': 'john'}

        bar_prefixed = PrefixedDict('bar', dictionary)
        foo_prefixed = PrefixedDict('foo', dictionary)

        self.assertEqual(set(foo_prefixed.keys()), set([]))
        self.assertEqual(set(bar_prefixed.keys()), set([]))

        foo_prefixed['gender'] = 'male'
        foo_prefixed['name'] = 'peter'

        self.assertEqual((set(foo_prefixed.keys())), set(['gender', 'name']))
        self.assertEqual(set(bar_prefixed.keys()), set([]))

        bar_prefixed['country'] = 'germany'
        bar_prefixed['email'] = 'peter@gmail.com'

        self.assertEqual(set(bar_prefixed.keys()), set(['country', 'email']))
        self.assertEqual(set(foo_prefixed.keys()), set(['gender', 'name']))

        self.assertEqual(set(dictionary.keys()),
                         set(['age', 'name',
                              'foo-gender', 'foo-name',
                              'bar-country', 'bar-email']))

    def test_values(self):
        dictionary = {'age': 30, 'name': 'john'}

        bar_prefixed = PrefixedDict('bar', dictionary)
        foo_prefixed = PrefixedDict('foo', dictionary)

        self.assertEqual(set(foo_prefixed.values()), set([]))
        self.assertEqual(set(bar_prefixed.values()), set([]))

        foo_prefixed['country'] = 'germany'

        self.assertEqual(set(foo_prefixed.values()), set(['germany']))
        self.assertEqual(set(bar_prefixed.values()), set([]))

        bar_prefixed['email'] = 'peter@gmail.com'

        self.assertEqual(set(bar_prefixed.values()), set(['peter@gmail.com']))
        self.assertEqual(set(foo_prefixed.values()), set(['germany']))

    def test_items(self):
        dictionary = {'age': 30, 'name': 'john'}

        bar_prefixed = PrefixedDict('bar', dictionary)
        foo_prefixed = PrefixedDict('foo', dictionary)

        self.assertEqual(set(bar_prefixed.items()), set([]))
        self.assertEqual(set(foo_prefixed.items()), set([]))

        bar_prefixed['country'] = 'germany'
        bar_prefixed['email'] = 'peter@gmail.com'

        self.assertEqual(set(bar_prefixed.items()),
                         set([('country', 'germany'),
                              ('email', 'peter@gmail.com')]))
        self.assertEqual(set(foo_prefixed.items()), set([]))

        foo_prefixed['age'] = 35
        foo_prefixed['name'] = 'peter'

        self.assertEqual(set(foo_prefixed.items()),
                         set([('age', 35),
                              ('name', 'peter')]))

    def test_keyerror(self):
        dictionary = {'email': 'peter@gmail.com'}

        prefixed = PrefixedDict('prefix', dictionary)

        with self.assertRaises(KeyError):
            prefixed['email']

    def test_in(self):
        dictionary = {'email': 'peter@gmail.com'}

        prefixed = PrefixedDict('prefix', dictionary)

        self.assertFalse('email' in prefixed)

        prefixed['name'] = 'peter'

        self.assertTrue('name' in prefixed)

    def test_iteration_on_keys(self):
        prefixed = PrefixedDict('prefix', {})
        prefixed['name'] = 'peter'
        prefixed['email'] = 'peter@gmail.com'

        self.assertEqual(set(prefixed.keys()),
                         set([key for key in prefixed]))

    def test_clear(self):
        dictionary = {'age': 30, 'name': 'john'}

        foo_prefixed = PrefixedDict('foo', dictionary)
        bar_prefixed = PrefixedDict('bar', dictionary)

        foo_prefixed['country'] = 'germany'
        foo_prefixed['email'] = 'peter@gmail.com'

        bar_prefixed['gender'] = 'male'
        bar_prefixed['city'] = 'berlin'

        foo_prefixed.clear()

        self.assertEqual(dict(foo_prefixed), {})

        self.assertEqual(dict(bar_prefixed),
                         {'gender': 'male', 'city': 'berlin'})

        self.assertEqual(dict(dictionary),
                         {'age': 30,
                          'name': 'john',
                          'bar-gender': 'male',
                          'bar-city': 'berlin'})

    def test_del(self):
        dictionary = {'age': 30, 'name': 'john'}

        foo_prefixed = PrefixedDict('foo', dictionary)
        bar_prefixed = PrefixedDict('bar', dictionary)

        foo_prefixed['country'] = 'netherlands'
        bar_prefixed['email'] = 'john@gmail.com'

        with self.assertRaises(KeyError):
            del foo_prefixed['age']

        with self.assertRaises(KeyError):
            del bar_prefixed['age']

        self.assertTrue('country' in foo_prefixed)
        del foo_prefixed['country']
        self.assertFalse('country' in foo_prefixed)

        self.assertTrue('email' in bar_prefixed)
        del bar_prefixed['email']
        self.assertFalse('email' in bar_prefixed)

        self.assertEqual(dictionary['age'], 30)
        self.assertEqual(dictionary['name'], 'john')
