"""
Отображения (mappings)

dict, defaultdict
"""

d = dict(foo='bar', spam='egg')
assert d == {'foo': 'bar', 'spam': 'egg'}

# доступ к элементам - по ключам
assert d['foo'] == 'bar'
assert d['spam'] == 'egg'

try:
    d['nothing'] = d['nothing']
except KeyError:
    print('ключа nothing нет в словаре')

# запись значений в существующий словарь
d['lol'] = 'tea'

# безопасный доступ к элементам
assert d.get('nothing') is None
assert d.get('nothing', 'something') == 'something'


for k in d:
    print(k, end=', ')  # foo, spam, lol (но необязательно в этом порядке)

for k in d.values():
    print(k, end=', ')  # bar, egg, tea  (но необязательно в этом порядке)

for k, v in d.items():
    print(k, '-', v, end=', ')  # foo - bar, spam - egg, lol - tea


# defaultdict - словарь с дефолтными значениями несуществующих ключей
from collections import defaultdict

loldict = defaultdict(lambda: 'lol')

assert loldict['foo'] == 'bar'
assert loldict['nothing'] == 'lol'
assert loldict[1] == 'lol'
assert loldict[None] == 'lol'

listdict = defaultdict(list)

loldict['great'].append(1)
assert loldict['great'] == [1]
assert loldict['python'] == []
