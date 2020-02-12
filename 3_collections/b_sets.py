"""
Множества - set, frozenset
"""

# set хранит только уникальные элементы
assert {1, 'a', 'a', 'b'} == set(['a', 'b', 1, 1, 'a', 'a']) == {'a', 'b', 1}

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd', 'e'}

# множествам недоступны слайсы и обращения по индексу
try:
    print(s1[0])
except Exception as e:
    print(type(e), e)

# операции со множествами
s1.remove('a')  # не найдёт - выбросит исключение
assert s1 == set('bc')

s1.add('a')
assert s1 == set('abc')
s1.add('a')
assert s1 == set('abc')

# самые интересные методы множеств
assert s1.difference(s2) == set('ab')  # чем отличается s1 от s2
assert s2.difference(s1) == set('de')  # чем отличается s2 от s1
assert s1.symmetric_difference(s2) == set('abde')  # полные различия вух множеств

assert s1.intersection(s2) == set('c')   # сходство двух множеств

# и т.д
