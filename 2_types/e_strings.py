"""
СТРОКИ
"""

# варианты записи
# одинарные и двойные скобки
# разница только в том, что при оборачивании строки в одинарные кавычки
# вы сможете использовать внутри строки двойные кавычки без экранирования
# и наоборот
print('single "quotes" string')
print("double 'quotes' string")

# multiline строка
print('''эта строка
может содержать переводы строки, 
идущие подряд одинарные ' или '' кавычки, и сколько угодно двойных """""""""''')

print("""эта строка
может содержать переводы строки, 
идущие подряд двойные " или "" кавычки, и сколько угодно одинарных '''''''''""")

# спецсимволы в строках
print('первая строка \n следующая строка \t табуляция')
# первая строка
#  следующая строка      табуляция

# экранирование в строках
print('первая строка \\n эта же строка \\t нет табуляции, \' - кавычка')
# первая строка \n эта же строка \t нет табуляции, ' - кавычка

# r-строки игнорируют спецсимволы
print(r'первая строка \n эта же строка \t нет табуляции, \' - кавычка')
# первая строка \n эта же строка \t нет табуляции, \' - кавычка


# работа со строками
s = 'knowledge'

# конкатенация
assert s + s == 'knowledgeknowledge'

# повторение
assert s * 3 == 'knowledgeknowledgeknowledge'

# выясняем длину строки
assert len(s) == 9

# доступ по индексу и слайсинг
assert s[0] == 'k'
assert s[1] == 'n'
assert s[-2] == 'g'

assert s[:2] == 'kn'
assert s[2:5] == 'owl'
assert s[5:] == 'edge'
assert s[:-4] == 'knowl'
assert s[::-1] == 'egdelwonk'  # простой способ инверсировать строку


#
# методы строки
#

# поиск первого вхождения подстроки (слева направо)
assert s.find('e') == s.find('edge') == 5
# поиск последнего вхождения подстроки (справа налево)
assert s.rfind('e') == 8
# более строгий аналог find/rfind - index/rindex. Вместо -1 выбрасывается ValueError
assert s.find('b') == -1  # если подстрока не найдена
assert s.count('e') == 2


# замена подстроки
assert s.replace('e', 'y') == 'knowlydgy'
assert s.replace('e', 'y', 1) == 'knowlydge'

# проверки
assert '123494132'.isdigit()
assert 'AbcXyz'.isalpha()
assert '123Abc'.isalnum()
assert 'abc de123'.islower()
assert 'ABC DE123'.isupper()
assert ' \f\n\r\t\v   '.isspace()
assert 'There Is No Knowledge, That Is Not Power'.istitle()
assert 'spam'.startswith('sp')
assert 'spam'.endswith('am')


# преобразования
assert 'egg'.upper() == 'EGG'
assert 'EGG'.lower() == 'egg'
assert 'my spam'.title() == 'My Spam'
assert 'my spam'.capitalize() == 'My spam'
assert 'spam'.center(10) == '   spam   '
assert 'spam'.center(10, '-') == '---spam---'
assert '\tegg\t'.expandtabs(4) == '    egg '
assert '  egg  '.lstrip() == 'egg  '
assert '  egg  '.rstrip() == '  egg'
assert '  egg  '.strip() == 'egg'
assert '-!--!!-egg-!-!!!---'.strip('-!') == 'egg'

assert ';'.join(['a', 'b', 'c']) == 'a;b;c'  # полезен на пратике

# форматирование
l = 'life'
t = 'throne'

assert '%s for %s' % (l, t) == 'life for throne'  # супер устаревшее
assert '{} for {}'.format(l, t) == 'life for throne'  # просто устаревшее
assert f'{l} for {t}' == 'life for throne'  # python >= 3.6
# https://shultais.education/blog/python-f-strings
# https://www.python.org/dev/peps/pep-0498/


# кодировки
assert 'Hello!'.encode('utf-8') == b'Hello!'
assert 'Привет!'.encode('utf-8') == b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'
assert 'Привет!'.encode('windows-1251') == b'\xcf\xf0\xe8\xe2\xe5\xf2!'
assert b'\xcf\xf0\xe8\xe2\xe5\xf2!'.decode('windows-1251') == 'Привет!'
