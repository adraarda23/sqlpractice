import sqlite3
conn = sqlite3.connect("rastgele.db")
c = conn.cursor()
kisiler1 = (12, 'nalbur', 3)
c.execute("""CREATE TABLE IF NOT EXISTS kisiler(
    id integer,
    isim text,
    numara integer
)
""")
c.execute("""INSERT INTO kisiler VALUES(15,'arda',1)
""")
c.execute("INSERT INTO kisiler VALUES(?,?,?)", kisiler1)
c.execute("INSERT INTO kisiler VALUES(?,?,?)", (1, 'melay', 12))
conn.commit()
conn.close()
