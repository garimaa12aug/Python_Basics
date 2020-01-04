# Lists are ordered sets of objects, whereas dictionaries are unordered sets. But the main difference is that items in dictionaries are accessed via keys and not via their position.
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(tel.keys())
print(sorted(tel.keys()))
print(sorted(tel.values()))
print('guido' in tel)
print('jack' not in tel)

'''
oyutput
{'jack': 4098, 'sape': 4139, 'guido': 4127}
4098
{'jack': 4098, 'irv': 4127, 'guido': 4127}
dict_keys(['jack', 'irv', 'guido'])
['guido', 'irv', 'jack']
[4098, 4127, 4127]
True
False
'''
