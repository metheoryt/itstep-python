"""
Собственные исключения
"""


class MyError(Exception):
    pass


class TooMuchArgumentsError(MyError):
    pass


def helloworlder():
    a = int(input('сколько раз написать hello world? '))
    if a < 0:
        raise MyError(f'{a} - не положительное число')
    if a > 10:
        raise TooMuchArgumentsError()
    for i in range(a):
        print('hello world!')


try:
    helloworlder()
except TooMuchArgumentsError:
    print('это число слишком большое')
except MyError as e:
    print(type(e), e)

try:
    helloworlder()
except Exception as e:
    print(type(e), e)
