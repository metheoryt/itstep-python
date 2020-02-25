"""
Флаги
"""

import re

# multiline
string = """foobar
foobaz
foobug
"""
print(re.findall('^foo', string))
print(re.findall('^foo', string, flags=re.MULTILINE))


# ignorecase
string = 'FooBar FooBaz FooLOL'
print(re.findall('[a-z]+', string))
print(re.findall('[a-z]+', string, flags=re.IGNORECASE))


# dotall
string = 'woe, \n it is me'
print(re.findall('.+', string))
print(re.findall('.+', string, flags=re.DOTALL))


# verbose
string = 'four.level.domain.name three.level.name. Hi!'
p = r"""
    (?<=[^\.])\b  # что угодно кроме точки перед началом слова
    (\w+\.){2}    # дважды часть домена с точкой
    [A-z]+        # домен первого уровня
    (?!\.\S)      # после него может быть что угодно, кроме точки, после которой идёт печатаемый знак
"""

results = re.finditer(p, string, flags=re.VERBOSE)

for r in results:
    print(repr(r).ljust(50), r.groups())

print(re.findall(p, string, flags=re.VERBOSE))
