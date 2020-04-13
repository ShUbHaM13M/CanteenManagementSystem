import sqlite3

db = sqlite3.connect(database="test.db")
cur = db.cursor()

cur.execute("create table if not exists test (No int NOT NULL, Name varchar2(100), Company varchar2(100), Price int, Quantity int, Discount float, primary key (No))")
print("table created")
no, name, company = 1, 'bisuits', 'parleg'
price, quantity, discount = 10, 10, 10.0
ls = (no, name, company, price, quantity, discount)
cur.execute(f"insert into test values(?, ?, ?, ?, ?, ?)", ls)
print("row inserted")

cur.execute("select * from test")
print(cur.fetchall())
