# prefixeddict

## why?
Sometimes you have a single dict-like object that will be used in multiple places, and you don't want one operation to redefine the values that were already set by another operation. So you use prefixes! The goal of this library it to make this as painless as possible.

## how?
```
>>> from prefixeddict import PrefixedDict
>>> my_dictionary = {}
>>> foo_prefixed = PrefixedDict('foo', my_dictionary)
>>> bar_prefixed = PrefixedDict('bar', my_dictionary)
>>> foo['age'] = 30
>>> bar['age'] = 50
>>> my_dictionary
{'foo-age': 30, 'bar-age': 50}
>>> foo['age']
30
>>> bar['age']
50
```

Available for Python 2.6+ and 3.2+. Simply run `pip install prefixeddict`.