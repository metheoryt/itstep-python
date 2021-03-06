"""
Якоря и флаги
"""
import re

# якоря - токены, обозначающие какие-либо места в строке
# \b - граница слова (word boundary)
string = 'the jet and jetski are noisy'
p = 'jet'  # найдёт jet в jetski
p = r'\bjet\b'  # найдёт только jet

r"""
^ - начало строки (или позиция после каждого \n с флагом re.MULTILINE)
$ - конец строки  (или позиция перед каждым  \n с флагом re.MULTILINE)
\A - абсолютное начало строки
\Z - абсолютный конец  строки
\b - граница слова
\B - инверсия границы слова
(?=e) - позитивная опережающая проверка
(?!e) - негативная опережающая проверка
(?<=e) - позитивная ретроспективная проверка
(?<!e) - негативная ретроспективная проверка
"""

# ретроспективная и опережающая проверки в деле
string = 'four.level.domain.name three.level.name. Hi!'
p = r'(?<=[^\.])\b(\w+\.){2}[A-z]+(?!\.\S)'


results = re.finditer(p, string)

for r in results:
    print(repr(r).ljust(50), r.groups())

