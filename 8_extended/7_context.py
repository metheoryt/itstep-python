"""
Менеджер контекста
"""

fh = None
try:
    fh = open('file.txt')
    for line in fh:
        print(line)
except Exception as e:
    print(e)
finally:
    if fh:
        fh.close()

# равнозначная запись
try:
    with open('filename.txt') as fh:
        for line in fh:
            print(line)
except Exception as e:
    print(e)

# Для того чтобы создать свой менеджер контекста
# из класса - определите спецметоды __enter__(self) и __exit__(self, exc_type, exc_value, tb_value)
# из функции - воспользуйтесь декоратором `contextlib.contextmanager`

# быстрое задание - напишите менеджер контекста, позволяющий делать несколько действий со списком атомарно
