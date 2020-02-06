"""
Функции, области видимости, ассерты
"""
import os


def my_func():
    # эту функцию можно назвать процедурой
    print('doing stuff...')


# docstring
def curdir_printer():
    """печатает в консоль абсолютный путь к текущей директории"""
    print(os.path.abspath('.'))


assert curdir_printer.__doc__ == 'печатает в консоль абсолютный путь к текущей директории'


# аннтотации типов
def strlen(s: str) -> int:
    return len(s)


assert strlen.__annotations__ == {'s': str, 'return': int}


# упаковка аргументов
def printer(*args, **kwargs):
    print(f'{args}; {kwargs}')


printer(1, 2)  # (1, 2); {}
printer(foo='a', bar='b')  # (); {'foo': 'a', 'bar': 'b'}
printer('a', None, egg=1)  # ('a', None); {'egg': 1}


def borgazer(arg1, arg2, *, foo):
    pass


borgazer(1, 2, 3)      # неправильно
borgazer(1, 2, foo=3)  # правильно
borgazer(arg1=1, arg2=2, foo=3)  # правильно


#
# распаковка аргументов
#
def summarizer(*args):
    return sum(args)


numbers = (55, 66)

print(summarizer(numbers[0], numbers[1]))  # правильно, но неудобно
print(summarizer(*numbers))                # правильно и удобно

users = {'johny': 'active', 'bruce': 'inactive'}
# распаковка позиционных аргументов - через *
# распаковка ключевых аргументов - через **
printer(*numbers, **users)


#
# Области видимости
#


# глобальная область видимости
foo = 'a'
bar = 'b'


def global_f():
    print(foo, bar)


global_f()  # a b


def local_f():
    # локальная область видимости
    foo = 'c'
    bar = 'd'
    print(foo, bar)


local_f()  # c d

#
cnt = 0


def global_changer_f():
    global spam, egg
    # чтобы перезаписать имя глобальной области видимости
    # из локальной области видимости,
    # нужно объявить его как global на первой строке тела функции
    spam += 'a'  # равнозначно spam = spam + 'a'
    egg += 'g'
    print(spam, egg)


# забавно, что вы можете определить имя
# после определения функции, перезаписывающей это имя.
# главное чтобы это было перед первым её вызовом, а то получите исключение NameError
spam = 'sp'
egg = 'e'

print(spam, egg)  # sp e
global_changer_f()  # spa eg
global_changer_f()  # spaa egg
print(spam, egg)     # spaa egg


def broken_counter_maker():
    # нелокальная область видимости
    num = 0

    def incrementer():
        # num объявлен в "нелокальной" области видимости (на уровень выше)
        num += 1  # эта строка вызовет исключение
        return num

    return incrementer


counter_f = broken_counter_maker()

try:
    counter_f()
except UnboundLocalError as e:
    print(e)  # local variable 'num' referenced before assignment


def counter_maker():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer


counter_f = counter_maker()

print(counter_f())  # 1
print(counter_f())  # 2


#
# Утверждения
#
# assert_stmt ::= "assert" expression1 ["," expression2]

assert (True, )
assert True
assert (True, 'это сообщение никогда не покажется')
assert True, 'это сообщение никогда не покажется'

try:
    assert False
except AssertionError as e:
    print(type(e), e)  # <class 'AssertionError'>

try:
    assert False, 'утверждение ложно'
except AssertionError as e:
    print(type(e), e)  # <class 'AssertionError'> утверждение ложно
    assert str(e) == 'утверждение ложно'

assert 1 == int('1')
assert 1 not in (2, 3)

# assert'ы можно отключить глобально,
# никогда не используйте их в бизнес-логике приложения!
# ощутите разницу:
# python -c "assert False"
# python -O -c "assert False"
