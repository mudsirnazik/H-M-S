from database import connect

def register(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

def login(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result
