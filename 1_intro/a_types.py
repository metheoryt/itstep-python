# Основные встроенные типы данных

# Неизменяемые (immutable)
n = None  # <class 'NoneType'> неопределённое (отсутствующее) значение, вроде NULL в sql
bo = True  # <class 'bool'>
s = 'py'  # <class 'str'>
by = b'py'  # <class 'bytes'> (есть изменяемый аналог - bytearray)
i = 2020  # <class 'int'>
f = 0.33  # <class 'float'>
c = 1+2j  # <class 'complex'>
t = (1, 2)  # <class 'tuple'> - контейнер

# Изменяемые (все - контейнеры)
l = [1, 2]                 # <class 'list'>
d = {1: 'spam', 2: 'egg'}  # <class 'dict'>
se = {1, 2}                # <class 'set'> (есть неизменяемый аналог set - frozenset)
