"""
Основы обработки исключений
"""

# базовый пример - отлавливаем и замалчиваем исключение (вместо исключения выведется сообщение в консоль)
try:
    # блок кода, способный выбросить исключение
    secret_number = 1 / 0
except ZeroDivisionError:
    # блок, в котором указанное исключение (и все его наследники) отлавливается
    print('снова не получилось разделить на ноль')


# не замалчиваем исключение
try:
    secret_number = 1 / 0
except ZeroDivisionError:
    print('сейчас упадёт')
    raise  # выбрасываем отловленное исключение


# получаем доступ к объекту исключения
some_list = []
try:
    secret_number = 1 / 0
    some_list.append(1)
except ZeroDivisionError as e:
    print(type(e), e)  # можем проанализировать отловленное исключение
    assert len(some_list) == 0  # код после строки, в которой выбросится исключение, не выполнится
    raise e  # или просто raise


# получаем доступ к объекту исключения
try:
    secret_number = 1 / 0
except ZeroDivisionError as e:
    print(type(e), e)  # можем проанализировать отловленное исключение
    raise e  # или просто raise

# отлавливаем несколько типов исключений разом
try:
    some_string = 'some string'
    if id(some_string) % 2 == 1:
        some_number = int(some_string)
    else:
        assert False, 'this should fail'
except (AssertionError, ValueError) as e:
    # в `e` будет объект одного из перечисленных типов, в зависимости от того, что именно отловилось
    print(type(e), e)
    raise


# обрабатываем разные типы исключений по разному
try:
    some_string = 'some string'
    if id(some_string) % 2 == 1:
        some_number = int(some_string)
    else:
        assert False, 'this should fail'
except AssertionError:
    print('получили assertion error')
except ValueError:
    print('не получилось преобразовать строку в int')


# else и finally
try:
    s = input('введите число: ')
    s = int(s)
except KeyboardInterrupt:
    # этот блок выполнится, если вы нажмёте ctrl+c пока скрипт будет ждать ввода (в pycharm может тупить)
    print('не хотите как хотите')
except ValueError:
    # этот блок выполнится, если то что вы ввели, не получится преобразовать в число
    print('вы ввели не число')
else:
    # этот блок выполнится, если блок try..except выполнится без исключений
    print(f'вы ввели число {s}!')
finally:
    # этот блок выполнится последним, в любом случае
    print('пока!')
