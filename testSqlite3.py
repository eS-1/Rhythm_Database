import sqlite3

connector = sqlite3.connect('test.sqlite3')
cur = connector.cursor()

# 以下SQL
# cur.execute('create table users(id integer, name text, title text, score real)')

# 書き込み
# cur.execute('insert into users values(1, "HentaiKusoDokata", "Unchi", 19.19)')

# 読み込み
# cur.execute('select * from users')
# data = cur.fetchall()
# print(data)

# 削除
# cur.execute('delete from users')

connector.commit()
connector.close()
