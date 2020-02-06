"""
Управление потоком выполнения
Условия и циклы
"""

# самый простой вариант
if True:
    print('этот блок выполнится т.к. условие удовлетворено')


# ветвление if-else
if len('spam') == 3:
    print('длина spam равна трём (?!)')
else:
    print('длина spam не равна трём')


color = 'красный'

# if-elif-else
if color == 'красный':
    print('огонь')
elif color == 'зелёный':
    print('трава')
elif color == 'синий':
    print('небо')
else:
    print('не знаю такого цвета')


# Циклы
#
# Цикл for
for i in range(10):  # range - генератор диапазона чисел
    # i - текущее число из диапазона
    print(f'эта строка напечатана {i + 1} раз(а)')

for char in ('a', 'b', 'c', 'd'):
    print(f'Саймон говорит "{char}"')


for letter in 'qwerty':
    if letter == 'e':
        continue  # при попадании на continue блок не дойдёт до конца и запустится следующая итерация
    if letter == 'r':
        break  # break полностью прерывает выполнение цикла
    print(letter)


# Цикл while - цикл с предусловием
# (когда нечего перебирать или количество попыток неизвестно)
counter = 0
while True:
    counter += 1
    print('А', end='')
    if counter == 100:
        print('!')
        break

# аналогично верхнему
counter = 0
while counter < 100:
    counter += 1
    print('А', end='')
    if counter == 100:
        print('!')
