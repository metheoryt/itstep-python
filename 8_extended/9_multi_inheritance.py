"""
Множественное наследование
разберём такую структуру наследования:

    Vars
   /    \
Foo      Bar
  \     /
   Spam

"""


# общий для всех класс
class Vars:
    def vars(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


class Foo(Vars):
    def __init__(self, x, *args):
        self.x = x
        # super(Foo, self).__init__(*args)

    def foo(self):
        print(f'foo from Foo! {self.vars()}')


class Bar(Vars):
    def __init__(self, a, *args):
        self.a = a
        # super(Bar, self).__init__(*args)

    def bar(self):
        print(f'bar from Bar! {self.vars()}')


# MRO слева направо - в каждом классе и его предках
class Spam(Foo, Bar):
    def __init__(self, egg):
        # super(Spam, self).__init__(egg)
        Foo.__init__(self, egg)
        Bar.__init__(self, egg)
        self.egg = egg

    def foo(self):
        super(Spam, self).foo()
        print('foo from Spam!')

    def bar(self):
        print('bar from Spam!')
        super(Spam, self).bar()


Spam(1).bar()
