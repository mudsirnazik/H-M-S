import sqlite3

def connect():
    return sqlite3.connect("hospital.db")

def setup():
    conn = connect()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS patients (id TEXT, name TEXT, age TEXT, disease TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS doctors (id TEXT, name TEXT, specialization TEXT)")

    conn.commit()
    conn.close()
