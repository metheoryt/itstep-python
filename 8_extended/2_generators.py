"""
Выражения-генераторы (generator expression)
Функции-генераторы
https://habr.com/ru/post/320288
"""

# генератор списка (list comprehension)
doubles = [v*2 for v in range(5)]
print(doubles)

# генератор словаря (dictionary comprehension)
the_names = {x: f'The {x}' for x in ['Simon', 'John', 'Alice']}
print(the_names)

# генератор множества (set comprehension)
the_names_set = {f'The {x}' for x in ['Simon', 'John', 'Alice']}
print(the_names_set)

# выражение-генератор (generator expression)
# выглядит как генератор кортежа, но возвращаемое значение - не кортеж,
# это генератор
generator = (v*2 for v in range(10))
print(generator)
print(list(generator))
