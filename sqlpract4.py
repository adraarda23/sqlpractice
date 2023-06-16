import sqlite3
conn = sqlite3.connect("arda.db")
c=conn.cursor()
conn.execute("""DELETE from kisiler WHERE rowid = 6
""")
conn.commit()