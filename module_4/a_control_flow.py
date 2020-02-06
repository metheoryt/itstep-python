"""
Управление потоком выполнения
Условия и циклы - подробнее
"""

users = {'fred': 'active', 'josh': 'inactive'}

# Изменение словаря в процессе итерации по нему
# вариант: итерироваться по копии словаря
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# вариант: создать новый словарь
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# доступ к индексу элемента
# вариант - использовать комбинацию функций range и len
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# вариант - использовать функцию enumerate
for i, v in enumerate(a):
    print(i, v)

#
# оператор pass
#
while True:
    pass  # бесконечный ничего не делающий цикл

for i in range(10):
    pass  #


# пустотелая функция
def my_func():
    pass


if 'foo' == 'bar':
    pass
else:
    print('foo != bar')


class MyClass:
    pass  # пустой класс
