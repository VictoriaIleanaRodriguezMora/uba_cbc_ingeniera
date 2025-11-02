- https://stackoverflow.com/questions/39465094/how-can-i-raise-an-error-if-input-is-nan
- https://www.turing.com/kb/nan-values-in-python
- https://stackoverflow.com/questions/41950021/typeerror-not-supported-between-instances-of-str-and-int
- https://www.reddit.com/r/learnpython/comments/kls9dh/exception_not_supported_between_instances_of_str/
- https://medium.com/@shilpasree209/the-keys-values-and-items-methods-in-python-dictionary-4c24cc3d26a7
- https://www.w3schools.com/python/python_dictionaries_methods.asp
- https://www.freecodecamp.org/news/how-to-check-if-a-key-exists-in-a-dictionary-in-python/
- https://www.freecodecamp.org/news/how-to-create-notice-blocks-in-markdown/


```py
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
# Output: dict_keys(['a', 'b', 'c'])

values = my_dict.values()
# Output: dict_values([1, 2, 3])

items = my_dict.items()
# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

```

`items()`	Returns a list containing a tuple for each key value pair
`keys()`	Returns a list containing the dictionary's keys

```py
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

try:
    value = my_dict['key1']
    print("Key exists in the dictionary.")
except KeyError:
    print("Key does not exist in the dictionary.")
```


