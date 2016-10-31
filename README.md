# prefixeddict [![Build Status](https://travis-ci.org/martinjungblut/prefixeddict.svg?branch=master)](https://travis-ci.org/martinjungblut/prefixeddict)
Prefixed dictionaries for Python 2.6+/3.2+.

## why?
Sometimes you have a single dict-like object that will be used in multiple places, and you don't want one operation to redefine the values that were already set by another operation. So you use prefixes! The goal of this library it to make this as painless as possible.

## how?
Install it: `pip install prefixeddict`

```
>>> from prefixeddict import PrefixedDict
>>> my_dictionary = {}
>>> foo_prefixed = PrefixedDict('foo', my_dictionary)
>>> bar_prefixed = PrefixedDict('bar', my_dictionary)
>>> foo_prefixed['age'] = 30
>>> bar_prefixed['age'] = 50
>>> my_dictionary
{'foo-age': 30, 'bar-age': 50}
>>> foo_prefixed['age']
30
>>> bar_prefixed['age']
50
```

## implementation details
This library is mostly lazy in order to improve memory allocation efficiency.
The keys(), values(), items() and \_\_iter\_\_() methods actually return iterators, not lists or another eager data structure.
The only method that currently uses an eager operation is clear().