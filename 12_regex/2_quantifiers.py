# Квантификаторы
import re

string = 'oh moon sooo gooood'


# pattern = 'o{2,5}'  # найдёт от двух до пяти повторений "o" в строке
# pattern = 'o{1}'  # 'o{1,1}'    - 'o'
# pattern = 'o{2}'  # 'o{2,2}'    - 'oo'
# pattern = 'o?'    # 'o{0,1}'  - необязательный 'o'
# pattern = 'o+'    # 'o{1,}'   - один или более 'o'
# pattern = 'o*'    # 'o{0,}'   - сколько угодно 'o' (в том числе и ни одного)

# квантификаторы по умолчанию "жадные" - ищут максимальное число совпадений
# "ленивый" режим квантификатора - найдёт минимальное совпадение
# pattern = 'o{2,3}'   # в строке 'ooooo' найдёт 'ooo'
# pattern = 'o{2,3}?'  # в строке 'ooooo' найдёт 'oo'


# комбинирование с символьными классами
# pattern = r'\w+'  # найдёт все слова в тексте
pattern = r'\d+'  # найдёт все числа в тексте


print('match:  ', re.match(pattern, string))
print('search: ', re.search(pattern, string))
print('findall:', re.findall(pattern, string))
