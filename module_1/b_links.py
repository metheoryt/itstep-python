"""
Ссылки на объекты

Переменная - это не контейнер значения, а имя, хранящее ссылку на объект.
"""

# изменяемые типы всегда создают новые объекты
l1 = [1, 2]
l2 = [1, 2]
assert l1 == l2
assert l1 is not l2  # хоть l1 и l2 равны, l1 не является l2 -  это разные объекты
print(f'l1 id is {id(l1)}')
print(f'l2 id is {id(l2)}')  # если id объектов совпадают - проверка на `is` вернёт True (и наоборот)

# кортежи идентичны пока все их элементы идентичны и неизменяемы
assert (1, 2, 'lol') is (1, 2, 'lol')
assert (1, 2, []) is not (1, 2, [])
assert (1, 2, l1) is not (1, 2, l1)

# изменяемые (mutable) объекты передаются по ссылке
l3 = l1
assert l3 is l1  # обе переменные хранят ссылку на один и тот же объект
assert id(l3) == id(l1)


# неизменяемые (immutable) объекты передаются по значению,
# но с оговоркой
a = 'knowledge wisdom understanding freedom'
b = 'knowledge wisdom understanding freedom'
assert a == b
assert a is b  # ???

b = a.lower()
assert a == b
assert a is not b  # TODO 3 кристалла каждому, кто выяснит почему так

# с числами немного по другому
assert 987654321 is 987654321
assert 987654321 is 987654320 + 1
assert 500000.33 is 500000.33
assert 500000.33 is 500000.32 + 0.01

# эти объекты-синглтоны всегда существуют в единственном экземпляре.
# ко всему прочему они ещё и ключевые слова
assert True is True
assert False is False
assert None is None
