import sqlite3
import os

db_path = 'db.sqlite3'

fresh_db = not os.path.exists(db_path)

conn = sqlite3.connect(db_path)  # подключение к БД
c = conn.cursor()  # курсор

if fresh_db:
    # если БД не существовала на момент проверки - выполним разовый setup
    print('БД пустая, создаём таблицы')
    c.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        pass TEXT NOT NULL
    )""")

c.execute('DELETE FROM users')

users_samples = ((f'alice{i}', f'mypass{i}') for i in range(10))

for u in users_samples:
    c.execute(f'INSERT INTO users (login, pass) VALUES (?, ?)', u)
    print(f'{u[0]} ID - {c.lastrowid}')

# ИЛИ
# c.executemany(f'INSERT INTO users (login, pass) VALUES (?, ?)', users_samples)


# каждую десятую алису меняем на боба
c.execute(f'UPDATE users SET login = ? WHERE id LIKE ?', ('bob', '%0'))

conn.commit()

# первые 10 пользователей
c.execute('SELECT * from users LIMIT 10')
print(c.fetchone())  # покажет первого в таблице
print(c.fetchone())  # покажет второго в таблице
# последние 10 пользователей
c.execute('SELECT * from users ORDER BY id DESC LIMIT 10')
print(c.fetchone())  # покажет последнего в таблице
print(c.fetchone())  # покажет предпоследнего в таблице


# курсор можно закрыть если он вам больше не нужен
c.close()
try:
    c.execute('SELECT 1')
except sqlite3.Error as e:
    print(e)  # и после этого его уже нельзя использовать


# не забывайте закрывать соединения (это не всегда обязательно но лучше это делать)
conn.close()
# при закрытии соединения все незафиксированные изменения (незакомиченные транзакции)
# откатятся (rollback) все открытые в соединении курсоры закроются автоматически
