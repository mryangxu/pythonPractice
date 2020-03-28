import sqlite3

try:
    conn = sqlite3.connect('test.db')

    cursor = conn.cursor()

    cursor.execute('select * from user where id=1', ())

    print(cursor)
    values = cursor.fetchall()

    print(values)

except BaseException:
    pass

finally:
    cursor.close()
    conn.close()