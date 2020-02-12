f = open('myfile.txt', 'w')  # r-w, a, b-t, +


for i in range(1, 10):
    for j in range(i):
        f.write(chr(65 + j))
    f.write('\n')

f.close()

try:
    f.write('sad')
except ValueError as e:
    print('no write sad,', e)  # файл уже закрыт

#
# Чтение контента
#
with open('myfile.txt', 'r') as f:  # with - менеджер контекста
    print(f)
    print(repr(f.read(12)))  # первые 12 символов
    print(repr(f.read(12)))  # следующие 12 символов
    print(repr(f.readline()))  # вполть до перевода строки (включительно)
    print(repr(f.readlines(2)))  # список из нескольких строк
    f.seek(0)  # вернёмся к началу файла
    print(repr(f.read(12)))  # снова прочтём первые 12 символов
    f.seek(30)  # прыгнем к 30-му символу
    print(repr(f.read(12)))  # прочтём 10 символов, начиная с 30-го

# после выхода из блока with файловый дескриптор автоматически закроется


try:
    f.read()
except ValueError as e:
    print('no read,', e)  # файл уже закрыт

# построчная работа с помощью цикла for
with open('myfile.txt') as f:
    for line in f:
        print(line)

# прочитать весь файл в список строк
with open('myfile.txt') as f:
    lines = f.readlines()
    print(lines[2])

# изменим одну строчку
lines[2] = 'foobar\n'

# записать список строк в файл
with open('myfile2.txt', 'w') as f:
    f.writelines(lines)
