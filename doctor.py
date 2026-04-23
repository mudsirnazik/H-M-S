from database import connect

def add_patient(pid, name, age, disease):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients VALUES (?,?,?,?)", (pid, name, age, disease))
    conn.commit()
    conn.close()

def get_patients():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    conn.close()
    return data

def add_doctor(did, name, spec):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO doctors VALUES (?,?,?)", (did, name, spec))
    conn.commit()
    conn.close()

def get_doctors():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctors")
    data = cur.fetchall()
    conn.close()
    return data
