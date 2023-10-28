# pylint: disable=missing-docstring, C0103
import sqlite3
import sys

conn = sqlite3.connect('data/movies.sqlite')
dbase = conn.cursor()

# Functions

def directors_count(db):
    # return the number of directors contained in the database
    query = """
    SELECT COUNT(name)from directors
    """
    db.execute(query)
    rows = db.fetchall()
    rowCount = rows[0][0]
    # print(rowCount)
    return rowCount

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = """
    SELECT name FROM directors
    order by name ASC
    """
    db.execute(query)
    rows = db.fetchall()
    name_list = [tup[0] for tup in rows]
    # print(name_list)
    return name_list


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """
    SELECT title from movies
    WHERE title LIKE "%love%" or title like ", love%"
    ORDER BY title ASC
    """
    db.execute(query)
    rows = db.fetchall()
    # print(rows)
    return rows


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    #word="by user"
    query = f"""
    SELECT COUNT(name) from directors
    WHERE UPPER(name) LIKE "%{name}%"
    """
    db.execute(query)
    rows = db.fetchall()
    # print(rows[0][0])
    return rows[0][0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"""
    SELECT title  from movies
    WHERE movies.minutes > "{min_length}"
    ORDER BY (title) ASC
    """
    db.execute(query)
    rows = db.fetchall()
    print(rows)
    return rows
conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
movies_longer_than(db, 300)



# Main
print(directors_count(dbase))
# print(directors_list(dbase))

if len(sys.argv) > 0:
    input_name = sys.argv[1]
    #print(directors_named_like_count(dbase, input_name))
else:
    print("type a word and rerun the command")

if len(sys.argv) > 0:
    input_min_length = sys.argv[1]
    #print(movies_longer_than(dbase, input_min_length))
else:
    print("type a duration and rerun the command")
