"""
Функторы - вызываемые объекты, способные хранить состояние
"""


# реализация через класс
class Strip:

    def __init__(self, characters: str):
        self.chars = characters

    def __call__(self, s: str):
        return s.strip(self.chars)


# реализация через замыкания
def stripper(chars: str):
    def strip(s: str):
        return s.strip(chars)
    return strip


import string

strip_punctuation_class = Strip(string.punctuation)
strip_punctuation_closure = stripper(string.punctuation)

assert strip_punctuation_class('.,,!VIP!,,.') == 'VIP'
assert strip_punctuation_closure('.,,!VIP!,,.') == 'VIP'
