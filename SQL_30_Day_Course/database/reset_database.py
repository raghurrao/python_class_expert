from pathlib import Path
import sqlite3
base=Path(__file__).resolve().parent
db=base/'university.db'
if db.exists(): db.unlink()
con=sqlite3.connect(db)
con.executescript((base/'schema.sql').read_text(encoding='utf-8'))
con.executescript((base/'seed_data.sql').read_text(encoding='utf-8'))
con.execute('PRAGMA foreign_keys=ON')
con.commit(); con.close()
print(f'Recreated {db}')
