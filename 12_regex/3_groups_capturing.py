import re

string = 'airplane is an aircraft as a jet is'

# выбор из альтернатив
p = 'airplane|aircraft|jet'

# группировка
#
# группы отвечают за группировку выражений и захват текста, попавшего в них
p = 'air(plane|craft)|jet'

# префикс ?: определяет не захватывающую группу (non-capturing group)
p = '(air(?:craft|plane)|jet)'

# к группам можно применять квантификаторы
string = 'senselessness'
p = 'sense([ln]ess)+'


# можно ссылаться на группы с помощью обратных ссылок (backreferencing)
# группы нумеруются начиная с 1,
# нумеруется каждая открывающаяся скобка слева направо
string = 'lol=lol foo=lol lol=foo foo=foo'
p = r'(\w+)=\1'

string = 'illness=ness senseless=less uselessness=lessness'
p = r'(\w+([ln]ess))=\2'

# именованные ссылки на группы
p = r'(\w+(?P<suffix>[ln]ess))=(?P=suffix)'


results = re.finditer(p, string)

for r in results:
    print(repr(r).ljust(50), r.groups())
