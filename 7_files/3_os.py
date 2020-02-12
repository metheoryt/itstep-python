import os

print(os.getcwd())  # текущая директория

if os.path.exists('myfile.txt'):  # проверить существование файла
    print('myfile.txt exists')

print(os.listdir('.'))

#
for f in os.walk('../7_files'):
    print(f)
