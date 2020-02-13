"""
Декораторы
Аннотации
"""
import time

#
# Декораторы
#


def performance(fn):

    def wrapper(*args, **kwargs):
        print(f'запускается функция {fn.__name__} c позиционными аргументами {args} и ключевыми {kwargs}')
        start_time = time.time()

        rvalue = fn(*args, **kwargs)

        end_time = time.time()
        print(f'функция {fn.__name__} выполнилась за {(end_time - start_time) * 1_000:.02f}ms')
        return rvalue

    return wrapper


def printer(arg):
    for i in range(100):
        v = [v for v in range(1000)]
    print(arg)


printer = performance(printer)

printer('lol')


@performance
def another_printer(arg):
    for i in range(100):
        v = [v for v in range(1000)]
    print(arg)


another_printer('lol')


#
# Аннотации
# https://habr.com/ru/company/lamoda/blog/432656/


def foo(bar: str, lol: int) -> bool:
    pass


q: str
x: str = '123'


class Foo:
    x: int
    y: int = 2

    @classmethod
    def factory(cls) -> 'Foo':
        return cls()

    def print_y(self):
        print(self.y)

    def print_x(self):
        print(self.x)

    def lol(self, another: 'Foo', b: str = 'aaa') -> bool:
        pass


f = Foo.factory()
f.print_y()

try:
    f.print_x()
except AttributeError as e:
    print(e)
