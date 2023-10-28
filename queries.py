# pylint: disable=missing-docstring, C0103
import sqlite3
import sys

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

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
    WHERE title LIKE '% love %'
        OR title LIKE '% love'
        OR title LIKE 'love %'
        OR title LIKE 'love,%'
        OR title LIKE '% love''%'
        OR title LIKE '% love.%'
        OR title LIKE 'love'
    ORDER BY title ASC
    """
    db.execute(query)
    rows = db.fetchall()
    # print(rows)
    return [tup[0] for tup in rows]


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
    return [tup[0] for tup in rows]
