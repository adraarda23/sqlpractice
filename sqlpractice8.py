import sqlite3
conn = sqlite3.connect("rastgele.db")
c = conn.cursor()
c.execute("""SELECT rowid, * FROM kisiler ORDER BY rowid DESC """)
for i in c.fetchall():
    print(i)
c.close()
