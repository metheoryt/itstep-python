"""
Последовательности
Списки, кортежи, именованные кортежи
"""

# создание списка
assert ['a', 'b', 'c'] == list(('a', 'b', 'c')) == list('abc')
lst = list('welcome!')

# все последовательности поддерживают слайсинг и доступ по индексу
assert lst[0] == 'e'
assert lst[1:3] == 'elc'
assert lst[-1] == '!'

# копирование списка/строки/кортежа (не рекурсивное)
new_lst_1 = lst[:]
new_lst_2 = lst.copy()  # аналогично для списка


assert lst.count('e') == 2  # считаем сколько раз такой элемент встречается в списке
assert lst.index('l') == 2


# списки - изменяемые объекты, большинство их методов ничего не возвращают
# а изменяют их состояние
lst.append('!')
assert lst == ['w', 'e', 'l', 'c', 'o', 'm', 'e', '!']
assert ''.join(lst) == 'welcome!'

lst.extend(['!', '!'])  # расширили исходный лист значениями другого листа
assert ''.join(lst) == 'welcome!!!'

assert lst.pop(len(lst) - 1) == '!'  # вытащили из списка последний элемент
assert ''.join(lst) == 'welcome!!'

lst.reverse()
assert ''.join(lst) == '!!emoclew'

lst.remove('!')  # удаляем первый такой элемент в списке. Если не найдет - выбросит исключение
assert ''.join(lst) == '!emoclew'

#
# Кортежи
#
# кортежи это как списки, только без методов по изменению своего состояния
assert ('a', 'b', 'c') == tuple('abc')
tp = tuple('welcome')
assert tp == ('w', 'e', 'l', 'c', 'o', 'm', 'e')

# кортеж из одного элемента
t1 = ('w', )  # запятая обязательна
t2 = 'w',     # можно без скобок (только при присвоении)
assert t1 == t2

#
# Именованные кортежи
#
from collections import namedtuple

User = namedtuple('User', ('login', 'email'))

petya = User('petya_xXx', 'petr666@mail.ru')

assert petya.login == petya[0] == 'petya_xXx'
assert petya.email == petya[1] == 'petr666@mail.ru'
