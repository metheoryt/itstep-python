"""
Декораторы
Аннотации
"""
import time

#
# Декораторы
#


# это декоратор
def performance(fn):

    def wrapper(*args, **kwargs):
        print(f'запускается функция {fn.__name__} c позиционными аргументами {args} и ключевыми {kwargs}')
        start_time = time.time()

        rvalue = fn(*args, **kwargs)

        end_time = time.time()
        print(f'функция {fn.__name__} выполнилась за {(end_time - start_time) * 1_000:.02f}ms')
        return rvalue

    return wrapper


# это наша декорируемая функция
def printer(arg):
    for i in range(100):
        v = [v for v in range(1000)]
    print(arg)


# декорирование функции - замена оригинальной функции обёрнутой
printer = performance(printer)

printer('lol')  # мы вызываем уже обёрнутую функцию (wrapper в декораторе performance)


# альтернативная (и основная) запись декорирования
@performance
def another_printer(arg):
    for i in range(100):
        v = [v for v in range(1000)]
    print(arg)


another_printer('lol')  # тот же самый эффект


#
# Декорирование класса
#

# декоратор класса принимает класс как аргумент
def class_performance(cls):
    # собираем все вызываемые атрибуты класса (в основном речь идёт о методах)
    # небольшой подводный камень - к методам, задекорированным как classmethod или staticmethod
    # лучше обращаться через getattr, нежели чем доставать их непосредственно из __dict__ класса.
    # Так вы дадите этим декораторам отработать и у вас будет ожидаемое поведение от ваших методов
    callable_attributes = {k: getattr(cls, k) for k in cls.__dict__.keys() if callable(getattr(cls, k))}
    # декорируем каждый такой метод нашим уже существующим декоратором
    for name, func in callable_attributes.items():
        decorated = performance(func)
        setattr(cls, name, decorated)  # и заменяем оригинальный метод декорированным!
    return cls


@class_performance
class Decorated:
    # теперь при вызове любого метода мы увидим в консоли сколько времени ушло на его выполнение!
    def spam(self):
        c = 0
        for i in range(1_000_000):
            c += i*2
        print(f'c is {c}')

    @classmethod
    def egg(cls):
        c = 0
        for i in range(2_000_000):
            c += i * 2
        print(f'c is {c}')

    @staticmethod
    def bread():
        c = 0
        for i in range(2_000_000):
            c += i * 2
        print(f'c is {c}')


Decorated().spam()
Decorated.egg()
Decorated.bread()


#
# Аннотации
# https://habr.com/ru/company/lamoda/blog/432656/
#


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
