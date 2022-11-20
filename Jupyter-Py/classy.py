import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute('''Create table if not exists Movies

# (Title TEXT, Director TEXT, year INT)''')

# cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchone())

# famousFilms = [('A', 'Scorsese', 1976), ('Back To the Future', 'Spielberg', 1985), ('Moonrise Kingdom', 'Anderson', 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)

# records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchall())

# for record in records:
#     print(record)


# def yearsAll():
#     rel_year = (1985,)

# yearsAll()

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

connection.commit()

connection.close()


