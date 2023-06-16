import sqlite3
conn = sqlite3.connect("arda.db")
c=conn.cursor()
c.execute(""" DROP TABLE kisiler""")
conn.commit()
conn.close()