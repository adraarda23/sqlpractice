import sqlite3

conn = sqlite3.connect("arda.db")
c = conn.cursor()


many_customers = [('Was', 'Sas', 'bus'), ('deym', 'geym', 'beym')]

c.execute("""CREATE TABLE IF NOT EXISTS kisiler(
    firstName text,
    lastName text,
    email text
)""")
c.execute("""INSERT INTO kisiler VALUES('Arda','Kilinc','arda.com')""")

#c.executemany("""INSERT INTO kisiler VALUES(?,?,?)""",many_customers)

conn.commit()   # commit edilmezse execute çalışmaz
conn.close()
