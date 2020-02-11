

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
        self.public_class = public  # в конструкторе объекта можно перезаписывать атрибуты класса
        self._protected = protected
        self._protected_class = protected
        self.__private = 'secret'

    # getter/setter свойства объекта
    @property
    def private_prop(self):
        return f'{self.__private}'

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

o.print_class_attrs()
o.print_object_attrs()

o.private_prop = 'password'
print(o.private_prop)

# можно обращатья к защищённым атрибутам напрямую, но это нежелательно
print(o._protected)
print(o.__private)  # ошибка
print(o._MyClass__private)  # приватный атрибут хранится здесь, но так делать не стоит

# с классом то же самое
print(MyClass._protected_class)
print(MyClass.__private_class)  # ошибка
print(MyClass._MyClass__private_class)


# динамическое присваивание метода классу
def dynamic_method(obj, x):
    print(f'obj.public is {obj.public} and x is {x}')


MyClass.method = dynamic_method

o.method(1)


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


john = John()

john.spam()
john.egg()

john.foo()  # ?
