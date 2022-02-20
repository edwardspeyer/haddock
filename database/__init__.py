import sqlite3

PATH = '/var/tmp/catdb.sqlite'


def connect():
    db = sqlite3.connect(PATH)
    db.executescript('create table if not exists cat(name unique, color);')
    return db


def get_by_name(name):
    db = connect()
    cur = db.execute('select * from cat where name = ?', [name])
    cats = list(cur)
    assert len(cats) == 1
    return cats[0]


def add_cat(name, color):
    db = connect()
    db.execute('insert or ignore into cat(name) values (?)', [name])
    db.execute('update cat set color = ? where name = ?', [color, name])
    db.commit()
