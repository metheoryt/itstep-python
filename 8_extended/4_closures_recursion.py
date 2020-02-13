"""
Вложенные функции (замыкания)
Рекурсивные функции
"""


def generate_power(power):  # функция-фабрика

    def nth_power(number):  # вложенная функция
        return number ** power

    return nth_power


pow_2 = generate_power(2)
pow_3 = generate_power(3)
print(pow_2(5))  # 5**2
print(pow_3(4))  # 4**3


# рекурсивная функция
def walk_dict(d):
    keys_count = len(d.keys())
    for v in d.values():
        if isinstance(v, dict):
            keys_count += walk_dict(v)
    return keys_count


d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'f': {
        'foo': 'bar',
        'lol': {
            'funk': 'fonk'
        },
        'egg': 'spam'
    }
}
print(d)
print('общее количество ключей словаря d: ', walk_dict(d))

# делаем "ВНИМАНИЕ" рекурсивный словарь - словарь, содержащий в одном из ключей ссылку на самого себя
d['d'] = d

print(d)

# рекурсивная функция с замыканием
def walk_dict_new(d, max_depth=5):
    """считает общее количество ключей в словаре, включая вложенные словари.
    если словарь глубже чем максимальная глубина вложенности max_depth - выбросится исключение"""

    current_depth = 0

    def inner_walk(_d):
        nonlocal current_depth
        current_depth += 1

        keys_count = len(d.keys())

        if current_depth > max_depth:
            current_depth -= 1
            return keys_count

        for v in d.values():
            if isinstance(v, dict):
                keys_count += inner_walk(v)

        current_depth -= 1
        return keys_count

    return inner_walk(d)


print('количество ключей рекурсивного словаря d с глубиной в 5 уровней:', walk_dict_new(d, max_depth=5))
print('количество ключей рекурсивного словаря d с глубиной в 10 уровней:', walk_dict_new(d, max_depth=10))
