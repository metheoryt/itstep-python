# Символы и классы символов
import re

string = """foxtrot firefox
unicorn
charlie
kilo 1 22 333 4444 55555 666666 7777777 88888888 999999999 0
"""


pattern = 'o'          # один символ
# pattern = 'fox'        # последовательность символов
# pattern = '[fox]'      # символьный класс (любой из перечисленных в квадратных скобках)
# pattern = '[a-z]'      # диапазон в символьном классе
# pattern = '[a-zA-Z]'   # несколько диапазонов в символьном классе
# pattern = '[0-2ki\n]'  # совмещение отдельных символов с диапазонами
# pattern = '[^A-z]'     # инверсия символьного класса "любой символ кроме перечисленных"

# сокращённые символьные классы
# pattern = '.'    # любой символ кроме \n (можно включить \n флагом re.DOTALL)
# pattern = r'\d'  # любое число, аналог [0-9]
# pattern = r'\D'  # [^0-9]
# pattern = r'\s'  # любой пробельный символ [\t\n\r\f\v]
# pattern = r'\S'  # [^\t\n\r\f\v]
# pattern = r'\w'  # любой символ "слова" [a-zA-Z0-9_]
# pattern = r'\W'  # [^a-zA-Z0-9_]


print('match:  ', re.match(pattern, string))
print('search: ', re.search(pattern, string))
print('findall:', re.findall(pattern, string))
