

# минимальная запись объявления класса
class TheClass:
    pass


egg = TheClass()

# проверка на тип
if isinstance(egg, TheClass):
    print('egg object is instance of TheClass class')


# наследование
class MyDict(dict):
    pass


dd = MyDict(foo='bar')
dd['key'] = 'value'
print(dd)  # {'foo': 'bar', 'key': 'value'}

# проверка на тип проверяет по всей ветке наследования
if isinstance(dd, MyDict):
    print('dd object is instance of MyDict class')
    if isinstance(dd, dict):
        print('dd object is instance of dict class')


# атрибуты и методы класса vs объекта
class MyClass:
    public_class = 'public class attribute'
    _protected_class = 'protected class attribute'
    __private_class = 'private class attribute'

    def __init__(self, public, protected):
        self.public = public  # атрибут объекта
        self._protected = protected
        self.__private = 'secret'

    # getter/setter свойства объекта
    @property
    def private_prop(self):
        return self.__private

    @private_prop.setter
    def private_prop(self, value):
        self.__private = f'secret {value}'

    # метод объекта
    def print_object_attrs(self):
        print(f'public attribute: {self.public!r}')
        print(f'protected attribute: {self._protected!r}')
        print(f'private attribute: {self.__private!r}')
        print(f'private property: {self.private_prop!r}')

    # метод класса
    @classmethod
    def print_class_attrs(cls):
        print(f'public class attribute: {cls.public_class!r}')
        print(f'protected class attribute: {cls._protected_class!r}')
        print(f'private class attribute: {cls.__private_class!r}')

    # статический метод
    @staticmethod
    def static_method():
        print('этот метод не привязан ни к объекту, ни к классу')

    def _protected_method(self):
        print('doing inner stuff')

    def __private_method(self):
        print('doing secret stuff')


MyClass.print_class_attrs()

o = MyClass(public='lol', protected='bar')

# эти два вызова равнозначны
o.print_object_attrs()
MyClass.print_object_attrs(o)


o.private_prop = 'password'
print(o.private_prop)  # secret password


# можно обращатья к защищённым атрибутам напрямую, но это нежелательно
print(o._protected)
print(o.__private)  # ошибка
print(o._MyClass__private)  # приватный атрибут хранится здесь, но так делать не стоит


# с атрибутами класса то же самое
print(MyClass._protected_class)
print(MyClass.__private_class)  # ошибка
print(MyClass._MyClass__private_class)


# динамическое присваивание метода классу
def dynamic_method(obj=None):
    if obj is not None:
        print(obj.foo)
    else:
        print('static')


class Dummy:
    foo = '42'


dum = Dummy()


Dummy.method = dynamic_method

dum.method()  # 42
Dummy.method(dum)  # 42
Dummy.method()  # static


#
# множественное наследование, MRO
#
class Spam:
    def foo(self):
        print('foo from Spam')

    def spam(self):
        print('the spam')


class Egg:
    def foo(self):
        print('foo from Egg')

    def egg(self):
        print('the egg')


class John(Spam, Egg):
    def foo(self):
        print('foo from John')


class Alice(Spam, Egg): pass


class Bob(Egg, Spam): pass


john = John()

john.spam()  # the spam
john.egg()  # the egg

john.foo()  # foo from John
Alice().foo()  # foo from Spam
Bob().foo()  # foo from Egg
