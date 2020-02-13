"""
Ветвление с использованием словарей
"""


color = input('цвет: ')

COLOR_ANIMAL = {
    'зелёный': 'крокодил',
    'белый': 'медведь',
    'красный': 'рак',
}

animal = COLOR_ANIMAL.get(color, 'кто угодно')

print(f'таким цветом может быть {animal}')


CALC = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

x, y, op = (
    int(input('левый операнд: ')),
    int(input('правый операнд: ')),
    input('операция: ')
)

if CALC.get(op):
    print(CALC[op](x, y))
else:
    print(f'операции {op} не найдено')
