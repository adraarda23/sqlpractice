import sqlite3
conn = sqlite3.connect("arda.db")
c=conn.cursor()
c.execute("""UPDATE kisiler SET firstName='Aydin' WHERE
rowid =2 AND lastName ='Kilinc'
""")
conn.commit()
conn.close()