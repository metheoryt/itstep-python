"""
динамическое исполнение кода
динамический импорт
https://habr.com/ru/post/221937/
"""

print('eval - динамическое исполнение кода')
eval('print("hello!")')

# eval может выполнить одно выражение за раз
# выражение - это однострочный кусок кода,
# результат выполнения которого вы можете присвоить переменной
x = eval(input('введите любое выражение: '))
print(f'результат - {x}')


stmt = """
try:
    x = int(x) * 10
except:
    x = 'exec исполняет код в текущей области видимости'
"""

exec(stmt)
# мы только что поменяли глобалюную переменную через exec
print(x)


# динамический импорт
import importlib

# import functools as f
f = importlib.import_module('functools')
print(f)

# import http.server as svr
svr = importlib.import_module('http.server')
print(svr)

# второй аргумент - пакет, относительно которого вы выполняете импорт модуля
path = importlib.import_module('.path', 'os')
print(path)
