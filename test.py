import sqlite3

connector = sqlite3.connect('test.sqlite3')
cur = connector.cursor()

users_data = [(2, "Kouji Tadokoro", "Senior", 19.19),
              (3, "Naoki Kimura", "Debut", 8.1),
              (4, "Daichi Miura", "Grand Senior", 114.514)]

# 以下SQL
# テーブル作成
# cur.execute('create table users(id integer, name text, title text, score real)')

# 書き込み
# cur.execute('insert into users values(1, "Taro Tanaka", "Debut", 0.0)')
# cur.executemany('insert into users values(?, ?, ?, ?)', users_data)

# 読み込み
# cur.execute('select * from users')
# data = cur.fetchall()
# print(data)

# 削除
# cur.execute('delete from users')
# cur.execute('delete from users where score < 10.0')

connector.commit()
connector.close()
