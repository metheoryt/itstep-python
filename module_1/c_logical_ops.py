"""
Логические операции

Операции, возвращащие в качестве результата булево значение - True/False
"""

# Приведение к bool
assert bool(0) is False
assert bool('') is False
assert bool([]) is False
assert bool(None) is False

assert bool(-1) is True
assert bool('a') is True
assert bool([1]) is True


# Сравнение
assert 2 > 1 is True
assert 2 < 1 is False
assert 2 == 2 is True
assert 2 != 2 is False
assert 3 >= 3 is True
assert 3 <= 4 is False


# составные выражения с помощью and-or-not
# https://docs.python.org/3/reference/expressions.html#operator-precedence
assert not 1 == 0  # not инвертирует значение
assert 2 == 2 and 3 != 2  # and вернёт True если оба операнда True (иначе False)
assert 2 == 2 or 3 == 2  # or вернёт True если хотя бы один операнд True (иначе False)

# is - вернёт True если оба операнда - один и тот же объект
assert 1 is 1

# in - вернёт True если операнд слева входит в операнд справа (обычно это коллекция)
assert 'black' in ['red', 'green', 'black']
assert 'black' in 'the black cat'  # так тоже можно
