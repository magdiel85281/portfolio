import mysql.connector as sql


def connection():
    conn = sql.connect(host='127.0.0.1', 
        user='root', 
        passwd='SQL@Ubuntu1', 
        db='portfolio')
    cur = conn.cursor()

    return cur, conn
