import sqlite3
conn = sqlite3.connect("arda.db")
c=conn.cursor()
c.execute("SELECT rowid,* FROM kisiler")

for i in c.fetchall():
    print(i)
c.close()