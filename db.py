import sqlite3

conn = sqlite3.connect("books.db")
conn.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key ,username text not null, password text not null )")
conn.execute("CREATE TABLE IF NOT EXISTS books(id integer primary key ,name text not null ,isbn integer)")
conn.execute("CREATE TABLE IF NOT EXISTS reviews(id integer primary key ,username text ,isbn integer)")
conn.execute("CREATE TABLE IF NOT EXISTS userbooks(id integer primary key ,username text ,password text,bookid integer,isbn integer)")
conn.execute("CREATE TABLE IF NOT EXISTS comments(bookid integer,comment text not null)")

conn.commit()
conn.close()
