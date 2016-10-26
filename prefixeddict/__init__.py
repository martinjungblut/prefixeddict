class PrefixedDict(object):
    """
    Prefixed dictionary, makes all keys be automatically prefixed with a given
    prefix.
    """

    def __init__(self, prefix, dictionary):
        """
        Args:
            prefix (str): the prefix you want to apply to the dictionary's
                          keys.
            dictionary (dict-like): the actual dictionary-like object which will
                                    be used to store data.
        """

        self.prefix = prefix + '-'
        self.dictionary = dictionary

    def __setitem__(self, key, value):
        self.dictionary[self.prefix + key] = value

    def __getitem__(self, key):
        return self.dictionary[self.prefix + key]

    def keys(self):
        return [key.replace(self.prefix, '') for key in self.dictionary.keys()]

    def values(self):
        return self.dictionary.values()

    def items(self):
        return zip(self.keys(), self.values())
