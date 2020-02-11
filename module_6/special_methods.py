class Multiplier:
    def __call__(self, x, y):
        return x*y


multiply = Multiplier()
multiply(19, 19)  # 361
# то же самое
multiply.__call__(19, 19)  # 361


class Collection:
    def __init__(self, _list):
        self.list = _list

    def __len__(self):
        return len(self.list)  # len вызывается на объекте списка


collection = Collection([1, 3, 5, 5, 1])
print(len(collection))


class SomeClass:
    attr1 = 42

    def __getattr__(self, attr):
        return attr.upper()


obj = SomeClass()
print(obj.attr1)  # 42
print(obj.attr2)  # ATTR2


class SomeClass2:
    attr1 = 42

    def __getattribute__(self, item):
        return item.upper()

    def __repr__(self):
        return f'SomeClass 2 {self.attr1}'

    def __str__(self):
        return f'SC2{self.attr1}'


obj = SomeClass2()
print(obj.attr1)  # ATTR1
print(obj.attr2)  # ATTR2

print(obj)  # SomeClass 2 ATTR1
print(str(obj))  # SC2ATTR1
